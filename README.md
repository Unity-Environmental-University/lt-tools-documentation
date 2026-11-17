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

If a tool repo is private, export a GitHub personal access token before building:

```bash
export GithubAccessToken=your_token_here
mkdocs serve
```

The GitHub Actions workflow reads the token from a repository secret named `GH_TOKEN` and passes it only to the build-and-deploy step in [.github/workflows/scheduled-deploy.yml](.github/workflows/scheduled-deploy.yml). The deploy token needs read-only access to the private `matt_lisa` repository.

## XR Education exports

The public portal imports Waste Management directly from its public
repository, including its interactive waypoint explainer. The four private
XR projects publish reviewed copies of selected pages under
[`docs/xr-education/`](docs/xr-education/). The portal build uses those copies
without needing access to the private XR repositories.

To update a private XR guide:

1. Make the edit under `docs/portal/` in the source repository. Preview it
   there with `mkdocs build --strict` using this portal's requirements.
2. Merge the source change into its `main` branch.
3. From this repository, run `python3 scripts/sync-xr-docs.py` with Git
   credentials that can read the four source repositories. If you add an
   exported page, list it in the script and this repository's navigation.
4. Review the exported changes for public release. Commit them with
   [the source revisions](xr-education-sources.json) and merge the portal
   change to rebuild the site.

The refresh copies only the listed pages. It leaves the current copies intact
if any source fetch fails. The portal config enables Mermaid for both exports
and imported pages.
