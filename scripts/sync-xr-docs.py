"""Refresh the public portal copies of explicitly listed private XR pages."""

import json
import subprocess
import tempfile
from pathlib import Path


ORGANIZATION = "Unity-Environmental-University"
PORTAL = Path(__file__).resolve().parents[1]
XR_DOCS = PORTAL / "docs" / "xr-education"

# Keep these lists and the XR Education navigation in mkdocs.yml in sync.
# Files outside this list never enter the public export.
EXPORTS = {
    "Summit": ("summit", ("index.md", "first-event.md", "unity.md", "data.md")),
    "Trailhead": ("trailhead", ("index.md", "first-replay.md", "unity.md", "recording.md")),
    "XR-Tools": ("xr-tools", ("index.md", "deploy.md", "development.md")),
    "XR-Tools-Updater-Service": ("xr-tools-updater-service", ("index.md", "verify.md")),
}


def main():
    pages = {}
    revisions = {}
    with tempfile.TemporaryDirectory(prefix="xr-docs-") as temp_dir:
        for repo, (section, filenames) in EXPORTS.items():
            url = f"https://github.com/{ORGANIZATION}/{repo}.git"
            checkout = Path(temp_dir) / repo
            subprocess.run(
                [
                    "git", "clone", "--quiet", "--depth=1", "--branch=main",
                    "--filter=blob:none", "--no-checkout", url, checkout,
                ],
                check=True,
            )
            commit = subprocess.check_output(
                ["git", "-C", checkout, "rev-parse", "HEAD"], text=True
            ).strip()
            revisions[f"{ORGANIZATION}/{repo}"] = commit

            for filename in filenames:
                pages[XR_DOCS / section / filename] = subprocess.check_output(
                    ["git", "-C", checkout, "show", f"{commit}:docs/portal/{filename}"]
                )

    # A failed clone or missing page leaves the checked-in export intact.
    for destination, content in pages.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
    (PORTAL / "xr-education-sources.json").write_text(
        json.dumps(revisions, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
