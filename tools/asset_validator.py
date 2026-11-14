"""Basic asset inventory and validation helper.

This first version deliberately validates file presence and supported formats.
Format-specific skeleton/material checks will be added with the production
asset-import pipeline in a later milestone.
"""
import argparse
import json
from pathlib import Path

SUPPORTED_MODEL_SUFFIXES = {".glb", ".gltf", ".bam", ".egg", ".obj"}


def inspect_assets(root: Path) -> dict:
    root = root.resolve()
    if not root.exists() or not root.is_dir():
        raise NotADirectoryError(f"Asset directory does not exist: {root}")

    files = sorted(path for path in root.rglob("*") if path.is_file())
    models = [path for path in files if path.suffix.lower() in SUPPORTED_MODEL_SUFFIXES]
    unsupported = [
        path for path in files
        if path.suffix.lower() in {".fbx", ".blend", ".max", ".ma", ".mb"}
    ]

    return {
        "asset_root": str(root),
        "file_count": len(files),
        "model_count": len(models),
        "models": [str(path.relative_to(root)) for path in models],
        "unsupported_source_files": [
            str(path.relative_to(root)) for path in unsupported
        ],
        "notes": [
            "This is an inventory check, not a full model, rig, animation, or material validator.",
            "Confirm each asset's licence and attribution requirements before use.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect ASHENVEIL asset files.")
    parser.add_argument("directory", nargs="?", default="assets")
    parser.add_argument("--output", help="Optional JSON report path.")
    args = parser.parse_args()

    report = inspect_assets(Path(args.directory))
    rendered = json.dumps(report, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
