# Replay a sample recording

Use the repository's sample recording to check ingestion, storage, and the 3D
viewer together. The sample has positions and events you can inspect as soon as
the upload finishes.

## Start Trailhead

1. From the repository root, copy `.env.example` to `.env`.
2. Set `DB_PASSWORD` and `API_KEY` to local test values.
3. Run `docker compose up --build -d`.
4. Open [the recordings gallery](http://localhost:8087/trailhead/recordings).

Compose starts PostgreSQL, applies the Trailhead migrations on application
startup, and mounts a volume for recording files.

## Upload the fixture

Set `API_KEY` in your shell to the value from the local `.env` file. Run the
command from the repository root.

```bash
base=http://localhost:8087/trailhead

curl --fail-with-body -sS "$base/api/recordings" \
  -H "Content-Type: application/json" \
  -H "x-api-key: $API_KEY" \
  --data-binary @fixtures/sample-recording.json
```

The response contains the new recording's `id`. Open
`http://localhost:8087/trailhead/recording?id=<id>` with that value.

Press **Play** and scrub backward to an earlier moment. Use the subject panel
to see what Trailhead tracked, and use the events panel to inspect a timestamp.
Reload the gallery to see the saved recording.

If the request returns `401`, check that the key in the shell matches the one
the container received. Check the `/trailhead` prefix if the request returns
`404`. Trailhead uses that prefix for both development and production builds.
