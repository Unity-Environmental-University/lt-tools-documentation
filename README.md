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

The GitHub Actions workflow reads the token from a repository secret named `GH_TOKEN` and passes it only to the build-and-deploy step in [.github/workflows/scheduled-deploy.yml](.github/workflows/scheduled-deploy.yml). The deploy token needs read access to `matt_lisa`. Use a fine-grained token
with read-only Contents access to the private repositories the portal imports.

## XR Education guides

The portal imports the public Waste Management guide with MkDocs Multirepo.
The XR Education overview links to the Summit, Trailhead, XR Tools, and XR
Tools Updater Service guides on GitHub. Readers need access to those repositories.

Each private project has a standalone `mkdocs.yml` and a `docs/portal/` directory.
To preview a guide, install this portal's requirements and run
`mkdocs serve` from the source repository's root.
