# XR Tools Updater Service

The updater service distributes signed XR Tools updates. Release CI sends a
Tauri manifest and platform bundle. An installed app asks whether it has an
update for its platform and current version.

```mermaid
sequenceDiagram
    participant C as XR Tools release workflow
    participant U as Updater service
    participant V as Release volume
    participant A as Installed XR Tools app
    C->>U: Send manifest and signed bundle
    U->>V: Store artifacts and update latest manifest
    A->>U: Check with target, architecture, and version
    U-->>A: Return download URL and signature for a newer build
    A->>U: Download the bundle
    Note over A: Tauri verifies the signature before installation
```

The service rewrites the manifest's download URLs to point at its hosted
artifacts. Uploads for the same version can add platform entries to the version's
manifest. The app-level manifest determines which version clients see.

See [Check an updater release](verify.md) for the API and a readiness check.
For server setup, use the [repository README](https://github.com/Unity-Environmental-University/XR-Tools-Updater-Service#readme).
