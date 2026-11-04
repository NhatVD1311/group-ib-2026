#!/usr/bin/env python3
"""Group-IB TI API client for CTF use.

Credentials: env GIB_USER / GIB_KEY, or tools/.gib_creds ("user:key" on one line).
Usage:
  python tools/gib.py get <path> [k=v ...]        raw GET, prints JSON
  python tools/gib.py search <term> [--deep]      search a term across text collections
  python tools/gib.py item <collection> <id>      fetch one record
"""
import base64, json, os, sys, time, urllib.parse, urllib.request, urllib.error

BASE = "https://tap.group-ib.com/api/v2/"
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "CTF/manual_1.0/gibctf_1.0/academic/urllib"
_last_call = {}


def creds():
    u, k = os.environ.get("GIB_USER"), os.environ.get("GIB_KEY")
    if u and k:
        return u, k
    with open(os.path.join(HERE, ".gib_creds"), encoding="utf-8") as f:
        u, k = f.read().strip().split(":", 1)
    return u, k


def get(path, params=None, raw=False, min_gap=1.1, retries=4):
    """GET with per-route throttling and 429 backoff."""
    for attempt in range(retries + 1):
        status, body = _get_once(path, params, min_gap)
        if status != 429 or attempt == retries:
            break
        time.sleep(3 * (attempt + 1))
    if raw:
        return status, body
    if status != 200:
        raise RuntimeError(f"HTTP {status} {path}: {body[:300]}")
    return json.loads(body)


def post(path, payload):
    """POST JSON (used by scoring/ip {"ips": [...]} and scoring/domain {"domains": [...]})."""
    u, k = creds()
    req = urllib.request.Request(BASE + path.lstrip("/"), data=json.dumps(payload).encode(), headers={
        "Authorization": "Basic " + base64.b64encode(f"{u}:{k}".encode()).decode(),
        "Accept": "application/json", "Content-Type": "application/json", "User-Agent": UA,
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} {path}: {e.read()[:300]!r}")


def _get_once(path, params, min_gap):
    """One throttled GET (API allows 1 req/s per feed, /search 1 per 10s)."""
    path = path.lstrip("/")
    route = path.split("?")[0]
    gap = 10.5 if route == "search" else min_gap
    wait = _last_call.get(route, 0) + gap - time.time()
    if wait > 0:
        time.sleep(wait)
    url = BASE + path
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params, doseq=True)
    u, k = creds()
    req = urllib.request.Request(url, headers={
        "Authorization": "Basic " + base64.b64encode(f"{u}:{k}".encode()).decode(),
        "Accept": "application/json",
        "User-Agent": UA,
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read().decode("utf-8", "replace")
            status = r.status
    except urllib.error.HTTPError as e:
        body, status = e.read().decode("utf-8", "replace"), e.code
    finally:
        _last_call[route] = time.time()
    return status, body


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    cmd = argv[1]
    if cmd == "get":
        params = dict(a.split("=", 1) for a in argv[3:])
        status, body = get(argv[2], params, raw=True)
        print(f"# HTTP {status}", file=sys.stderr)
        try:
            print(json.dumps(json.loads(body), ensure_ascii=False, indent=1))
        except ValueError:
            print(body)
    elif cmd == "item":
        print(json.dumps(get(f"{argv[2]}/{argv[3]}"), ensure_ascii=False, indent=1))
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
