# Learning Technology Tools Documentation

![docs](https://github.com/Unity-Environmental-University/lt-tools-documentation/actions/workflows/scheduled-deploy.yml/badge.svg)

This repo is the central hub that publishes the [LXD Tools Portal](https://unity-environmental-university.github.io/lt-tools-documentation/). It uses [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and the [mkdocs-multirepo-plugin](https://github.com/jdoiro3/mkdocs-multirepo-plugin) to pull documentation from individual tool repositories and combine them into a single site.

## How it works

The site is defined in [mkdocs.yml](mkdocs.yml). Each tool's docs live in its own GitHub repository under a `docs/` folder. The `multirepo` plugin fetches those docs at build time using `!import` entries in the `nav` section. GitHub Actions builds and deploys the site to GitHub Pages on every push to `main`. The deploy action also runs every Sunday so developers don't have to run a push to main here to update their documentation. If documentation needs to be updated sooner, there is a Run workflow button in `Actions` -> `Deploy MK-Docs Site`.

## Adding a new tool

1. **Prepare the tool's repository** — Add a `docs/` folder to the tool's repo. MkDocs expects at least one `.md` file there.
    A mkdocs.yml file is required at the root of the repository. It needs at least a `nav` section mapping page names to actual docs files.
    ```yaml
    nav:
      - Getting Started: README.md
      - Frontend Design: FRONTEND_README.md
      - Backend Design: BACKEND_README.md
    ```

2. **Register the tool here** — Open [mkdocs.yml](mkdocs.yml) and add an entry to the `nav` section:

   ```yaml
   nav:
     - Home: index.md
     - My New Tool: "!import https://github.com/your-org/your-repo?branch=main"
   ```

   Replace the URL and branch with the tool repo's actual values.

3. **Update the portal homepage** — Edit [docs/index.md](docs/index.md) to add a row for the new tool in the "What's here" table.

4. **Push to `main`** — The GitHub Actions workflow triggers automatically and redeploys the site.

## Writing docs for a tool

Documentation lives inside each tool's own repository, not this one. To update or add content for a tool:

- Navigate to that tool's repo and edit files under its `docs/` folder.
- Use standard Markdown. MkDocs Material supports [extended syntax](https://squidfunk.github.io/mkdocs-material/reference/).
- The portal rebuilds automatically when this repo is pushed to `main` and every Sunday. To pick up tool-repo changes sooner, use the Run workflow button for [.github/workflows/scheduled-deploy.yml](.github/workflows/scheduled-deploy.yml) in this repo's `Actions` tab.

## Local development

```bash
pip install -r requirements.txt
mkdocs serve
```

The site is available at `http://127.0.0.1:8000`. Changes to `docs/index.md` or `mkdocs.yml` reload automatically; changes in imported repos require a restart.

## Private repositories

To build locally, use Git credentials with read access to the source
repositories. The GitHub CLI credential helper can reuse your existing login.

```bash
gh auth setup-git
mkdocs build --strict
```

The GitHub Actions workflow maps the portal repository's `GH_TOKEN` secret to
`GithubAccessToken` during the build. Use a token with **Contents: Read-only**
access to the following Unity Environmental University repositories.

- `matt_lisa`
- `Summit`
- `Trailhead`
- `XR-Tools`
- `XR-Tools-Updater-Service`

Verify the new credential can read all five before replacing the current
secret in **Settings → Secrets and variables → Actions**.

## XR Education source docs

Write Summit, Trailhead, XR Tools, and XR Tools Updater Service guides in
`docs/portal/` in the respective repositories. The portal imports that
directory from each repository's `main` branch. Add new pages to that
repository's `mkdocs.yml` navigation and preview them with
`mkdocs build --strict` using this portal's requirements. Every file in
`docs/portal/` is eligible for publication on the public portal.

Waste Management uses its public `docs/` directory, including the
interactive waypoint explainer. The portal config enables Mermaid for all
imported guides. After a source change merges, the next scheduled or manual
portal build picks it up.
