# Record from Unity

Add [`TrailheadRecorder.cs`](https://github.com/Unity-Environmental-University/Trailhead/blob/main/clients/unity/TrailheadRecorder.cs)
to a persistent GameObject. Configure `apiUrl` with the Trailhead base URL,
including `/trailhead`. Set `apiKey` to the server's recording upload key.
The example logs the payload size in the Editor. Run a player build to upload.

## Track the objects that explain a session

1. Call `Identify(playerId)` with a stable pseudonymous ID.
2. Call `StartRecording("Forest walkthrough")`.
3. Call `AddSubject("Player", playerCamera.transform)` and save the returned index.
4. Mark a meaningful moment with `AddSubjectEvent(playerIndex, "Checkpoint reached")`.
5. Call `FinishRecording()` when play ends.

The subject index identifies the tracked object, even if other subjects have the
same name. Use `AddEvent` for events that apply to the entire recording and
`SetMetadata` for context such as the game mode. Use `ClearSubjects` between
sessions when each session registers its own objects.

Subscribe to `OnUploadComplete` before finishing the recording. If it returns
an ID, open `GetReplayUrl(id)` in the browser. The example client sends one
complete file. Clients that need to save progress during browser play can use
the [segmented upload route](recording.md#ingest-routes).

## Keep the Summit session attached

When Summit and Trailhead run in the same game, use the same player ID for
both. Subscribe to Summit's `OnSessionStarted` before starting its session.
Call Trailhead's `LinkSummitSession(sessionId, playerId)` with the ID from the
callback. When the server syncs the recording summary, Summit can attach it
to the original session.

See the [Unity recorder guide](https://github.com/Unity-Environmental-University/Trailhead/tree/main/clients/unity#readme)
for render metadata and a complete code example.
