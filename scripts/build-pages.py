#!/usr/bin/env python3
"""Publish the latest versioned portfolio at the GitHub Pages root."""

import argparse
import re
import shutil
from pathlib import Path


def build(output_name: str) -> None:
    root = Path(__file__).resolve().parents[1]
    output = (root / output_name).resolve()
    if output.parent != root or not output.name.startswith("_site"):
        raise ValueError("Output must be an _site build directory directly inside the repository")

    versions = [
        (int(path.parent.name[1:]), path)
        for path in (root / "demo").glob("v*/index.html")
        if re.fullmatch(r"v[0-9]+", path.parent.name)
    ]
    if not versions:
        raise ValueError("No versioned portfolio found in demo/v*/index.html")
    version, source = max(versions)
    html = source.read_text(encoding="utf-8")
    old_assets = 'const IMG = "../../assets/previews/";'
    if html.count(old_assets) != 1:
        raise ValueError("The portfolio asset path changed; review the root-page mapping before publishing")
    html = html.replace(old_assets, 'const IMG = "./assets/previews/";')

    images = set(re.findall(r'"img"\s*:\s*"([^"/]+)"', html))
    images.add("profile-cutout.png")
    for image in images:
        if not (root / "assets" / "previews" / image).is_file():
            raise FileNotFoundError(f"Missing portfolio image: {image}")

    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    shutil.copytree(root / "assets", output / "assets")
    shutil.copytree(root / "demo", output / "demo")
    (output / "index.html").write_text(html, encoding="utf-8")
    (output / ".nojekyll").touch()
    print(f"Published demo/v{version}/index.html at / with {len(images)} verified images")
    print(f"Output: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="_site")
    build(parser.parse_args().output)
