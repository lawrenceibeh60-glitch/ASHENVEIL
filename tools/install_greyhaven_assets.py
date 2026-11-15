"""Download and validate the Greyhaven building pack from its GitHub Release.

Run from the repository root:
    python tools/install_greyhaven_assets.py
"""
from __future__ import annotations

import argparse
import struct
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URL = (
    "https://github.com/lawrenceibeh60-glitch/ASHENVEIL/releases/download/"
    "greyhaven-assets-v1/building_pack_free_low-poly_3d_model_in_fbx.glb"
)
DEFAULT_DESTINATION = (
    PROJECT_ROOT
    / "assets"
    / "environments"
    / "greyhaven"
    / "building_pack_free_low-poly_3d_model_in_fbx.glb"
)


def validate_glb(path: Path) -> None:
    """Reject incomplete downloads and files that are not glTF binary v2."""
    with path.open("rb") as stream:
        header = stream.read(12)
    if len(header) != 12:
        raise ValueError("Downloaded file is too small to be a GLB file.")
    magic, version, declared_length = struct.unpack("<4sII", header)
    actual_length = path.stat().st_size
    if magic != b"glTF":
        raise ValueError("Downloaded file does not have the GLB magic header.")
    if version != 2:
        raise ValueError(f"Expected GLB version 2, received version {version}.")
    if declared_length != actual_length:
        raise ValueError(
            f"GLB length mismatch: header says {declared_length}, "
            f"file contains {actual_length} bytes."
        )


def install_asset(url: str, destination: Path, force: bool = False) -> Path:
    """Download to a temporary file, validate it, then atomically install it."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not force:
        validate_glb(destination)
        print(f"Asset already installed and valid: {destination}")
        return destination

    temporary = destination.with_suffix(destination.suffix + ".download")
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ASHENVEIL-Asset-Installer/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            with temporary.open("wb") as output:
                while chunk := response.read(1024 * 1024):
                    output.write(chunk)
        validate_glb(temporary)
        temporary.replace(destination)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise

    print(f"Installed and validated: {destination}")
    print(f"Size: {destination.stat().st_size:,} bytes")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DEFAULT_URL, help="Release asset URL")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_DESTINATION,
        help="Destination GLB path",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing valid asset",
    )
    args = parser.parse_args()
    install_asset(args.url, args.output, force=args.force)


if __name__ == "__main__":
    main()
