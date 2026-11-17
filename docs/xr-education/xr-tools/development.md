# Develop and release XR Tools

## Run the desktop app

Install Node.js, Rust, and the native prerequisites for Tauri on your
platform. Run these commands from the repository root.

```sh
npm ci
npm run dev
```

Use `npm run build` to produce a desktop bundle. Use `npm run web:dev` for
Vite-only interface work and the desktop window to exercise commands that
call Rust.

| Area | Source |
| --- | --- |
| Tool interface and update prompt | [`src/main.js`](https://github.com/Unity-Environmental-University/XR-Tools/blob/main/src/main.js) |
| Native commands and VCS integration | [`src-tauri/src/tools/`](https://github.com/Unity-Environmental-University/XR-Tools/tree/main/src-tauri/src/tools) |
| Installers and signed updater bundles | [Release workflow](https://github.com/Unity-Environmental-University/XR-Tools/blob/main/.github/workflows/release.yml) |

## Verify a release

1. Run **Release** from the repository's Actions tab with the intended version.
2. Check the GitHub release for the Linux, Windows, and macOS installers.
3. Check the updater service for the Windows x86-64 and Apple Silicon bundles.
4. Open an older compatible desktop build. On launch, check that it offers
   the new version, then install it and confirm the app reports the new version.

The workflow points the packaged app at the configured HTTPS updater service.
The app verifies the downloaded update against its embedded public key. Keep
the matching signing key available to the release workflow. See the
[repository setup instructions](https://github.com/Unity-Environmental-University/XR-Tools#auto-updates)
for local updater testing and GitHub secret names.
