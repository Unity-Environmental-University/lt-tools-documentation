# Summit data and reporting reference

## Data Summit collects

| Record | What it describes | Where to look |
| --- | --- | --- |
| Session | A play interval for an app, with version, player ID, and session metadata | Sessions |
| Event | A named action with optional properties, measurements, or a numeric value | Events Explorer |
| Performance sample | Client FPS and memory observations | Performance |
| Hardware profile | Device information associated with a player across sessions | Users |
| Feedback response | Answers keyed by the fields of a form or supplied by the game | Feedback |
| Trailhead summary | A recording ID, metadata, and a replay URL when configured | Sessions or Users |

An event with an unknown session ID or a session ID from a different app can
still appear in Events Explorer. Summit stores that event without a session
association. For an integrated replay, the UUID in `summit_session_id` identifies
the Summit session, while the Trailhead recording has its own UUID.

## Where to answer a question

| Question | View |
| --- | --- |
| What happened around a specific action? | Open the session and inspect its event timeline. Follow its replay link if one is available. |
| At which step do players stop a sequence? | Build a funnel from the ordered event names. |
| Does frame rate vary across sessions? | Compare FPS in Performance and inspect specific players in Users. |
| What did players report? | Filter Feedback and inspect response details and per-question rollups. |
| Which fields recur in a weekly report? | Build a custom report from stored fields, save the definition, and export its results as CSV. |

## API entry points

Paths are relative to the application base path. Game ingestion uses the
game's app key in `x-api-key`. Programmatic dashboard queries and app management
use the dashboard API key. Browser access uses a signed-in dashboard account.

| Operation | Route |
| --- | --- |
| Start or end a session | `POST /api/ingest/session/start` or `POST /api/ingest/session/end` |
| Record events or samples | `POST /api/ingest` or `POST /api/ingest/batch` |
| Send device details | `POST /api/ingest/hardware` |
| Load a feedback form or send answers | `GET /api/feedback/forms` or `POST /api/ingest/feedback` |
| Query recorded events | `POST /api/query/events` |
| Run a custom report definition | `POST /api/reports/run` |

See the [full API table](https://github.com/Unity-Environmental-University/Summit#api-endpoints)
and the [request schemas](https://github.com/Unity-Environmental-University/Summit/blob/main/dashboard/lib/validation.ts)
for route-specific fields.
