"""Small admin tasks against the running PDS, with its admin password. Standard library only.

    PDS_URL=https://pds.mundusnovus.org PDS_ADMIN_PASSWORD=... python3 scripts/admin.py health
    ... python3 scripts/admin.py invite                 one single-use invite code
    ... python3 scripts/admin.py account <did>          details of one account
    ... python3 scripts/admin.py takedown <did>         suspend an account (undo with: restore <did>)
"""
import base64, json, os, sys, urllib.request

URL = os.environ.get("PDS_URL", "http://localhost:3000").rstrip("/")
AUTH = "Basic " + base64.b64encode(("admin:" + os.environ.get("PDS_ADMIN_PASSWORD", "")).encode()).decode()


def xrpc(method, nsid, body=None, params=""):
    req = urllib.request.Request(URL + "/xrpc/" + nsid + params, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"authorization": AUTH, "content-type": "application/json"})
    with urllib.request.urlopen(req) as r:
        text = r.read().decode()
        return json.loads(text) if text else {}


def status(did, on):
    return xrpc("POST", "com.atproto.admin.updateSubjectStatus", {"subject": {"$type": "com.atproto.admin.defs#repoRef", "did": did}, "takedown": {"applied": on}})


if __name__ == "__main__":
    cmd, arg = (sys.argv + ["", ""])[1:3]
    out = {"health": lambda: xrpc("GET", "_health"),
           "invite": lambda: xrpc("POST", "com.atproto.server.createInviteCode", {"useCount": 1}),
           "account": lambda: xrpc("GET", "com.atproto.admin.getAccountInfo", params="?did=" + arg),
           "takedown": lambda: status(arg, True),
           "restore": lambda: status(arg, False)}.get(cmd)
    if not out:
        sys.exit(__doc__)
    print(json.dumps(out(), indent=1))
