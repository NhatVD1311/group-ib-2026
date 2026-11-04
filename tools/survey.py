import json, sys, time
sys.path.insert(0, "tools")
import gib
cols = [x["collection"] for x in gib.get("user/granted_collections")]
out = {}
for c in cols:
    st, body = gib.get(f"{c}/updated", {"limit": 1}, raw=True)
    try:
        j = json.loads(body)
    except ValueError:
        j = None
    info = {"status": st}
    if isinstance(j, dict):
        info["topkeys"] = list(j.keys())[:8]
        info["count"] = j.get("count")
        items = j.get("items") or []
        if items:
            info["itemkeys"] = list(items[0].keys())
            info["sample"] = json.dumps(items[0], ensure_ascii=False)[:400]
    else:
        info["body"] = body[:150]
    out[c] = info
    print(c, st, info.get("count"), (info.get("itemkeys") or [])[:12], info.get("body", ""), flush=True)
    time.sleep(0.4)
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
