# The Asteria account server: the official AT Protocol PDS from Bluesky, configured for Railway.
# Accounts, posts, follows and pictures live here, in each person's own repository, so they can move them to any
# other PDS whenever they like. Settings come from the environment; see README.md and .env.example.
FROM ghcr.io/bluesky-social/pds:0.4
LABEL org.opencontainers.image.title="Asteria Technology PDS" org.opencontainers.image.licenses="MIT AND Apache-2.0"
ENV PDS_PORT=3000 \
    PDS_DATA_DIRECTORY=/pds \
    PDS_BLOBSTORE_DISK_LOCATION=/pds/blocks \
    PDS_BLOB_UPLOAD_LIMIT=5242880 \
    PDS_INVITE_REQUIRED=true \
    PDS_DID_PLC_URL=https://plc.directory \
    PDS_BSKY_APP_VIEW_URL=https://api.bsky.app \
    PDS_BSKY_APP_VIEW_DID=did:web:api.bsky.app \
    PDS_REPORT_SERVICE_URL=https://mod.bsky.app \
    PDS_REPORT_SERVICE_DID=did:plc:ar7c4by46qjdydhdevvrndac \
    PDS_CRAWLERS=https://bsky.network \
    LOG_ENABLED=true
EXPOSE 3000
