#!/usr/bin/env python3
"""Scan Group-IB TI for one or more terms and print a readable report.

  python tools/scan.py <term> [<term> ...] [--pages N] [--all] [--out DIR]

Term type is auto-detected (ip / domain / email / hash / url / text) and decides
which collections are queried. Every matching item is saved raw to --out
(default: out/<term>/), and a pivot list (emails, domains, IPs, nicknames,
Telegram handles, links) is printed for the next hop.

--all        also query low-yield collections (vulns, deface, ddos, proxies...)
--pages      max pages of 100 items per collection (default 3)
--no-follow  don't open threat actors referenced by hits (default: open them and
             read every report, since feed search only reaches ~30 days back)
"""
import argparse, html, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gib

# Collections with text search worth hitting for any term. Order = report order.
TEXT_COLS = [
    "hi/threat_actor", "hi/threat", "apt/threat_actor", "apt/threat",
    "hi/open_threats", "hi/analytic", "malware/malware", "common/threat_landscape",
    "ioc/primary", "malware/cnc", "malware/config", "malware/signature",
    "attacks/phishing_kit", "attacks/phishing_group",
    # "Individual" collections: usually empty for this account, cheap to check
    "darkweb/forums", "compromised/messenger", "compromised/discord", "compromised/access",
]
EXTRA_COLS = [
    "attacks/deface", "attacks/ddos", "osi/vulnerability", "malware/yara",
    "common/threat_actor", "common/threat",
]
IP_COLS = ["suspicious_ip/scanner", "suspicious_ip/tor_node", "suspicious_ip/vpn",
           "suspicious_ip/open_proxy", "suspicious_ip/socks_proxy"]

FREEMAIL = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "proton.me",
            "protonmail.com", "mail.ru", "yandex.ru", "icloud.com"}

RE_IP = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")
RE_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)
RE_HASH = re.compile(r"^([a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64})$", re.I)
RE_DOMAIN = re.compile(r"^(?=.{3,253}$)([a-z0-9-]+\.)+[a-z]{2,}$", re.I)

PIVOT_RES = {
    "email": re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    "telegram": re.compile(r"(?:t\.me/|telegram\.me/)([A-Za-z0-9_+]{3,})"),
    "url": re.compile(r"https?://[^\s\"'<>\\]+"),
    "ip": re.compile(r"\b\d{1,3}(?:\[?\.\]?\d{1,3}){3}\b"),
}


def kind(term):
    t = term.strip().replace("[.]", ".")
    if RE_IP.match(t):
        return "ip"
    if RE_EMAIL.match(t):
        return "email"
    if RE_HASH.match(t):
        return "hash"
    if t.lower().startswith(("http://", "https://")):
        return "url"
    if RE_DOMAIN.match(t):
        return "domain"
    return "text"


def qvariants(term, k):
    """Unquoted terms are tokenized (an email also matches every gmail.com record), so
    quote anything with punctuation; for plain words also try a trailing wildcard
    (leading wildcards are rejected with HTTP 400)."""
    if k == "text" and re.fullmatch(r"[\w-]+", term):
        return [term, f"{term}*"]
    return [f'"{term}"']


def fetch(col, q, pages):
    items, seq = [], 0
    for _ in range(pages):
        status, body = gib.get(f"{col}/updated", {"q": q, "limit": 100, "seqUpdate": seq}, raw=True)
        if status != 200:
            return items, f"HTTP {status} {body[:80].strip()}"
        j = json.loads(body)
        batch = j.get("items") or []
        items += batch
        if len(batch) < 100 or j.get("seqUpdate") in (None, seq):
            break
        seq = j["seqUpdate"]
    return items, None


def summarize(col, it):
    """One-line human summary of a record."""
    g = it.get
    if col.endswith("threat_actor"):
        st = g("stat") or {}
        return (f"[ACTOR] {g('name')} aka={g('aliases')} country={g('country')} "
                f"seen={st.get('dateFirstSeen')}..{st.get('dateLastSeen')} expertise={st.get('expertise')} "
                f"malware={st.get('malware')}")
    if col.endswith("/threat"):
        ta = (g("threatActor") or {}).get("name")
        return f"[REPORT {g('datePublished')}] {g('title')} | actor={ta} | id={g('id')}"
    if col == "hi/open_threats":
        a = g("author") or {}
        return f"[OPEN {str(g('dateDetected'))[:10]}] {a.get('screenName') or g('source')} {g('link')} :: {(g('text') or g('title') or '')[:160]!r}"
    if col.startswith("malware/malware"):
        return f"[MALWARE] {g('name')} aliases={g('aliases')} platform={g('platform')} actors={g('threatActorList')}"
    if col.startswith("ioc/"):
        return f"[IOC {g('type')}] {g('domain') or g('url') or g('ip') or g('hash')} malware={g('malwareList')} actors={g('threatActorList')}"
    if col == "malware/cnc":
        return f"[C2] {g('cnc')} ip={g('ipv4')} malware={g('malwareList')} actor={g('threatActor')}"
    if "phishing_kit" in col:
        return f"[KIT] {g('hash')} brand={g('targetBrand')} emails={g('emails')} tg={g('telegramIds')} from={g('downloadedFrom')}"
    if col == "attacks/phishing_group":
        return f"[PHISH] {g('domain')} brand={g('brand')} ip={g('ip')}"
    keys = ("title", "name", "siteUrl", "domain", "ipv4", "id")
    return f"[{col}] " + " ".join(f"{k}={g(k)}" for k in keys if g(k))[:220]


def pivots(blobs, term):
    found = {k: set() for k in PIVOT_RES}
    found["nickname"] = set()
    for b in blobs:
        s = json.dumps(b, ensure_ascii=False)
        for k, rx in PIVOT_RES.items():
            for m in rx.findall(s):
                found[k].add(m.replace("[.]", ".").rstrip(".,);"))
        for fa in b.get("forumsAccounts") or []:
            found["nickname"].add(f"{fa.get('nickname')} @ {fa.get('url')}")
        for c in b.get("contacts") or []:
            found["nickname"].add(f"{c.get('service')}:{c.get('account')} ({c.get('flag')})")
        ta = b.get("threatActor")
        if isinstance(ta, dict) and ta.get("name"):
            found["nickname"].add(f"actor:{ta['name']}")
    noise = ("group-ib.com", "schema.org", "w3.org")
    res = {k: sorted(v for v in vs if (term.lower() not in v.lower() or k == "nickname")
                     and not any(n in v for n in noise))
           for k, vs in found.items()}
    return {k: v for k, v in res.items() if v}


def whois_digest(j):
    rows = []
    for h in (j.get("whois_history") or []) + (j.get("whois") or []):
        recs = h.get("data") or [h]
        for r in recs:
            vals = {p["field"]: p["value"] for p in r.get("parsed", []) if p.get("value")}
            if vals:
                rows.append((r.get("checked_at") or r.get("first_seen") or h.get("first_seen"), vals))
    return rows


def enrich(term, k, out):
    t = term.replace("[.]", ".")
    if k == "email" and t.split("@")[-1].lower() in FREEMAIL:
        return
    if k in ("domain", "url", "email"):
        dom = re.sub(r"^https?://", "", t).split("/")[0].split("@")[-1]
        sld = ".".join(dom.split(".")[-2:])
        try:
            j = gib.get("utils/graph/domain", {"domain": sld})
            save(out, "whois_domain", j)
            print(f"\n## WHOIS {sld} (created {j.get('created_at')})")
            for when, vals in whois_digest(j):
                print(f"  {when}: " + "; ".join(f"{a}={','.join(map(str, v))}" for a, v in vals.items()))
        except Exception as e:
            print(f"  whois {sld}: {e}")
        try:
            print("  score:", gib.post("scoring/domain", {"domains": [sld]}).get("items"))
        except Exception as e:
            print("  score:", e)
    if k == "ip":
        try:
            j = gib.get("utils/graph/ip", {"ip": t})
            save(out, "whois_ip", j)
            print(f"\n## WHOIS {t} ({j.get('start')}-{j.get('end')} {j.get('provider')})")
            seen = set()
            for when, vals in whois_digest(j):
                line = "; ".join(f"{a}={','.join(map(str, v))}" for a, v in vals.items()
                                 if a in ("netname", "descr", "country", "org", "org-name", "address", "e-mail", "abuse-mailbox", "person", "role"))
                if line and line not in seen:
                    seen.add(line)
                    print(f"  {when}: {line}")
            print("  score:", gib.post("scoring/ip", {"ips": [t]}).get("items"))
        except Exception as e:
            print(f"  whois/score {t}: {e}")


def html_text(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def actor_ids(items):
    """Threat-actor ids referenced by any record (feeds only search ~30 days back,
    but direct GET by id reaches older actors and reports)."""
    ids = {}
    for it in items:
        refs = []
        for key in ("threatActorList", "taList", "relatedThreatActors", "threatActors"):
            v = it.get(key)
            refs += v if isinstance(v, list) else []
        if isinstance(it.get("threatActor"), dict):
            refs.append(it["threatActor"])
        elif isinstance(it.get("threatActor"), list):
            refs += it["threatActor"]
        for r in refs:
            if isinstance(r, dict) and r.get("id"):
                ids[r["id"]] = (r.get("name"), bool(r.get("isAPT")))
    return ids


def report_text(rid, apt=False):
    r = gib.get(f"{'apt' if apt else 'hi'}/threat/{rid}")
    return r, html_text(r.get("description"))


def follow_actors(ids, needle, out, max_reports):
    for aid, (name, apt) in list(ids.items())[:8]:
        col = "apt/threat_actor" if apt else "hi/threat_actor"
        status, body = gib.get(f"{col}/{aid}", raw=True)
        if status != 200:
            print(f"\n## ACTOR {name} {aid}: HTTP {status}")
            continue
        a = json.loads(body)
        save(out, f"actor_{name or aid}", a)
        st = a.get("stat") or {}
        print(f"\n## ACTOR {a.get('name')} ({aid}) aka={a.get('aliases')} country={a.get('country')} "
              f"seen={st.get('dateFirstSeen')}..{st.get('dateLastSeen')} expertise={st.get('expertise')}")
        print("   " + html_text(a.get("description"))[:700])
        for r in (st.get("reports") or [])[:max_reports]:
            title = (r.get("name") or {}).get("en") or r.get("name")
            try:
                rep, text = report_text(r["id"], apt)
            except Exception as e:
                print(f"   - {r['datePublished']} {title}: {e}")
                continue
            save(out, f"report_{r['id']}", rep)
            with open(os.path.join(out, f"report_{r['id']}.txt"), "w", encoding="utf-8") as f:
                f.write(f"{rep.get('title')}\n{rep.get('sources')}\n\n{text}")
            contacts = [c.get("account") for c in rep.get("contacts") or []]
            fa = [f.get("nickname") for f in rep.get("forumsAccounts") or []]
            print(f"   - {r['datePublished']} {title} [{r['id']}] contacts={contacts} forums={fa}")
            pat = re.escape(needle).replace(r"\.", r"(?:\.|\[\.\])")  # reports defang IOCs
            for m in list(re.finditer(pat, text, re.I))[:3]:
                print(f"       ...{text[max(0, m.start() - 200):m.end() + 300]}...")


def save(out, name, obj):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name.replace("/", "_") + ".json"), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


def scan(term, pages, all_cols, out_root, follow=True, max_reports=10):
    k = kind(term)
    out = os.path.join(out_root, re.sub(r"[^\w.@-]+", "_", term))
    cols = TEXT_COLS + (EXTRA_COLS if all_cols else []) + (IP_COLS if k == "ip" else [])
    print(f"\n# SCAN {term!r}  type={k}  -> {out}")
    enrich(term, k, out)
    needle = term.lower().replace("[.]", ".")
    every = []
    for col in cols:
        merged, err = {}, None
        for q in qvariants(term, k):
            items, err = fetch(col, q, pages)
            for it in items:
                merged[it.get("id") or json.dumps(it)[:80]] = it
        if not merged:
            if err:
                print(f"  {col}: {err}")
            continue
        items = list(merged.values())
        exact = [it for it in items if needle in json.dumps(it, ensure_ascii=False).lower()]
        save(out, col, items)
        print(f"\n## {col}: {len(items)} hit(s), {len(exact)} contain the literal term")
        for it in (exact or items)[:25]:
            print("  " + summarize(col, it))
        every += exact
    if follow:
        follow_actors(actor_ids(every), needle, out, max_reports)
    pv = pivots(every, term)
    if pv:
        print("\n## PIVOTS (from records containing the term)")
        for k2, vs in pv.items():
            print(f"  {k2}: " + ", ".join(vs[:40]))
    save(out, "_pivots", pv)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="+")
    ap.add_argument("--pages", type=int, default=3)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--no-follow", action="store_true", help="don't open linked actors/reports")
    ap.add_argument("--reports", type=int, default=10, help="max reports per linked actor")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "out"))
    a = ap.parse_args()
    for t in a.terms:
        scan(t, a.pages, a.all, a.out, not a.no_follow, a.reports)


if __name__ == "__main__":
    main()
