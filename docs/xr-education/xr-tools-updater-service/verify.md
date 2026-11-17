# Check an updater release

## Read the manifest and check the platform

Set `UPDATER_URL` to the HTTPS service URL for a test environment. Check that
the service responds, then inspect the manifest for the app.

```sh
curl --fail-with-body -sS "$UPDATER_URL/health"
curl --fail-with-body -sS "$UPDATER_URL/api/apps/xr-tools/static/latest.json"
```

If the environment requires client authentication, send the configured bearer
token with the manifest, update-check, and download requests.

Choose a version lower than the manifest version. For example, if the manifest
promotes a version above `3.0.0`, check the Apple Silicon entry this way.

```sh
curl --fail-with-body -i "$UPDATER_URL/api/apps/xr-tools/check/darwin/aarch64/3.0.0"
```

Expect `200` with a version, download URL, and signature when a newer bundle
exists for that platform. Repeat with the manifest version and expect
`204`. A newer version without a bundle for the requested platform returns
`404`. Confirm that each expected platform is present after release jobs finish.

## Service reference

| Route | Purpose |
| --- | --- |
| `GET /health` | Confirm the server can open its data directory |
| `POST /api/apps/{appId}/releases` | Accept a multipart manifest and its referenced files using the upload bearer token |
| `GET /api/apps/{appId}/static/latest.json` | Read the latest manifest across platforms |
| `GET /api/apps/{appId}/check/{target}/{arch}/{currentVersion}` | Get a newer bundle entry for one platform |
| `GET /download/{appId}/{version}/{asset}` | Download a stored release artifact |

`DATA_DIR` is the persistent storage root. Set `BASE_URL` to the HTTPS origin
that clients use to reach the service, so the manifest's download URLs resolve
from the desktop app. `UPLOAD_TOKEN` authorizes release CI. The optional
`CLIENT_AUTH_TOKEN` applies to manifest reads, update checks, and downloads.
