# Send your first event

Create a disposable app and send an event you can find in Events Explorer.
Use the Docker stack so the service runs with the same `/summit` path as a
production build.

## Start Summit

1. From the repository root, copy `.env.example` to `.env`.
2. Set `DB_PASSWORD`, `DASHBOARD_API_KEY`, and `SUMMIT_ADMIN_PASSWORD` in `.env`.
3. Run `docker compose up -d`.
4. Open [the local dashboard](http://localhost:8088/summit/dashboard) and sign
   in with the bootstrap administrator account.

On a new stack, PostgreSQL initializes the schema. For database upgrades, follow
the [migration notes in the repository](https://github.com/Unity-Environmental-University/Summit#readme)
for the database you are upgrading.

## Create an app and session

Run these commands from a terminal. Set `DASHBOARD_API_KEY` in your shell to
the value from the local `.env` file before you begin.

```bash
base=http://localhost:8088/summit

curl --fail-with-body -sS "$base/api/apps" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $DASHBOARD_API_KEY" \
  -d '{"name":"Documentation smoke test"}'
```

Set `APP_API_KEY` in your shell to the returned `api_key`. Run the next request
with the app key. The response includes the new session's `id`.

```bash
curl --fail-with-body -sS "$base/api/ingest/session/start" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $APP_API_KEY" \
  -d '{"user_id":"docs-player","app_version":"0.0.1"}'
```

## Track a checkpoint

Set `SESSION_ID` to the returned `id`. Send one event to that session.

```bash
curl --fail-with-body -sS "$base/api/ingest" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $APP_API_KEY" \
  --data-binary @- <<JSON
{"events":[{"name":"checkpoint_reached","session_id":"$SESSION_ID","user_id":"docs-player","properties":{"checkpoint":"trail_marker","measurements":{"elapsed_seconds":42}}}]}
JSON
```

Open the test app in Summit. In Events Explorer, find `checkpoint_reached` and
check the checkpoint and measurement on the event. In Sessions, open the
session and find the same event on its timeline.

If the request returns `401`, check which key the endpoint expects. If it
returns `404`, check the base path. A direct Next.js development server serves
routes at `/api/…`, while Docker serves them at `/summit/api/…`.
