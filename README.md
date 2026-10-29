# ChristianSystemsPDS

The account server behind **Christian Systems Social**. It is the official
[AT Protocol PDS](https://github.com/bluesky-social/pds) from Bluesky, set up to run on Railway.

Each person's account, posts, likes, follows and pictures are kept here in their own signed repository. Because it
is the open AT Protocol, people can move their account to another server whenever they like, and what they post can
be seen across the wider network.

Social (in ChristianSystemsOrg) creates accounts here and writes every record here on each person's behalf. Social
only keeps an index for feeds, search, notifications, messages and moderation.

## Deploy on Railway

1. Make a service from this repository. Railway builds the `Dockerfile`.
2. Add a **volume** mounted at `/pds`. Everything lives there: keep Railway's volume backups on.
3. Make the secrets:

   ```bash
   python3 scripts/make_secrets.py
   ```

   Add them, with the two names from `.env.example`, to the service's variables. Keep a private copy of all three.
4. Add the custom domain `pds.christiansystems.org`, and a wildcard `*.pds.christiansystems.org`, so each handle
   (`name.pds.christiansystems.org`) can prove itself. Railway shows the DNS records to add.
5. Check it: `https://pds.christiansystems.org/xrpc/_health` answers with its version.
6. In the Social service (ChristianSystemsOrg), set `PDS_URL` to that address and `PDS_ADMIN_PASSWORD` to the same
   admin password.

New accounts need an invite code. Social makes a single-use code for each account it creates, so nobody else can
sign up on this server directly.

## Look after it

```bash
PDS_URL=https://pds.christiansystems.org PDS_ADMIN_PASSWORD=... python3 scripts/admin.py health
```

`scripts/admin.py` also makes invite codes, looks up an account, and suspends or restores one. Social's moderators
suspend accounts from its moderation page, which does the same thing.

To update the PDS, change the version in the `Dockerfile` (`ghcr.io/bluesky-social/pds:0.4`) after reading
Bluesky's release notes, and redeploy.

## License

Our files here are under the **Christian Systems License 1.0** (GPL-3.0-only); see [LICENSING.md](LICENSING.md).
The PDS itself is Bluesky's, under the MIT and Apache 2.0 licenses.
