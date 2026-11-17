# XR Education tools

A player places a defense in SludgeTower. Summit can count that placement
across sessions. Trailhead can show where it happened on the board and which
objects moved around it. The two views use the same Summit session ID to
take you from an analytics question to a moment you can replay.

```mermaid
flowchart TB
    Game["Unity player build"]
    Game -->|Events, sessions, feedback| Summit["Summit"]
    Game -->|Object motion and timeline events| Trailhead["Trailhead"]
    Trailhead -->|Recording summary and session ID| Summit
    Summit -->|Open a replay| Trailhead
    Summit -->|Reports and event timelines| Team["XR Education team"]
    Trailhead -->|3D replay| Team
```

## Find the right guide

Summit, Trailhead, XR Tools, and XR Tools Updater Service open on GitHub.
Sign in with access to the corresponding repository to read those guides.

| I want to | Open |
| --- | --- |
| Send analytics or see what players do across sessions | [Summit](https://github.com/Unity-Environmental-University/Summit/blob/main/docs/portal/index.md) |
| Record tracked objects or inspect a specific play session | [Trailhead](https://github.com/Unity-Environmental-University/Trailhead/blob/main/docs/portal/index.md) |
| Trace the board and waypoint paths in a working Unity example | [Waste Management](waste-management/index.md) |
| Upload a web build or work on the desktop utilities | [XR Tools](https://github.com/Unity-Environmental-University/XR-Tools/blob/main/docs/portal/index.md) |
| Check a signed desktop update for a platform | [XR Tools Updater Service](https://github.com/Unity-Environmental-University/XR-Tools-Updater-Service/blob/main/docs/portal/index.md) |

## Trace a game session

1. Give both Unity clients the same pseudonymous player ID.
2. When Summit returns a session UUID, attach it to the Trailhead recording.
3. Send analytics to Summit and replay data to Trailhead during or after play,
   according to the recording client in the game.
4. Open the session in Summit and follow the Trailhead link after the summary
   sync. The replay's recording ID is separate from the Summit session UUID.

[Connect Summit and Trailhead in Unity](https://github.com/Unity-Environmental-University/Summit/blob/main/docs/portal/unity.md) or try the
[SludgeTower verification walkthrough](waste-management/verify.md). For
experience-specific material, see the existing
[Unity XR user documentation](https://github.com/Unity-Environmental-University/XR-User-Documentation)
and the [Horticulture developer docs](https://github.com/Unity-Environmental-University/Horticulture-Scripts/tree/main/docs).

## Ship the build and update the desktop app

```mermaid
flowchart LR
    Build["Unity web build"] --> XR["XR Tools desktop"]
    XR -->|FTPS upload| Host["Game hosting"]
    CI["XR Tools release workflow"] -->|Signed desktop artifacts| Installer["GitHub Releases"]
    CI -->|Signed update bundles| Service["XR Tools Updater Service"]
    XR -->|Check version and platform| Service
    Service -->|Bundle URL and signature| XR
```

XR Tools uploads web builds. Its updater service distributes new versions of
the XR Tools desktop app. Use the [test deployment guide](https://github.com/Unity-Environmental-University/XR-Tools/blob/main/docs/portal/deploy.md)
for a web build and the [updater checks](https://github.com/Unity-Environmental-University/XR-Tools-Updater-Service/blob/main/docs/portal/verify.md) for
a desktop release.
