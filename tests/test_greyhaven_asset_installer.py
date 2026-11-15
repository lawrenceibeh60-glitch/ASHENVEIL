"""Tests for the Greyhaven GLB download validator."""
import struct

import pytest

from tools.install_greyhaven_assets import validate_glb


def write_glb_header(path, *, magic=b"glTF", version=2, declared_length=12):
    path.write_bytes(struct.pack("<4sII", magic, version, declared_length))


def test_validate_glb_accepts_valid_binary_v2(tmp_path):
    path = tmp_path / "valid.glb"
    write_glb_header(path)
    validate_glb(path)


@pytest.mark.parametrize(
    ("magic", "version", "declared_length", "message"),
    [
        (b"nope", 2, 12, "magic"),
        (b"glTF", 1, 12, "version"),
        (b"glTF", 2, 99, "length mismatch"),
    ],
)
def test_validate_glb_rejects_invalid_header(
    tmp_path, magic, version, declared_length, message
):
    path = tmp_path / "invalid.glb"
    write_glb_header(
        path,
        magic=magic,
        version=version,
        declared_length=declared_length,
    )
    with pytest.raises(ValueError, match=message):
        validate_glb(path)


def test_validate_glb_rejects_truncated_file(tmp_path):
    path = tmp_path / "truncated.glb"
    path.write_bytes(b"glTF")
    with pytest.raises(ValueError, match="too small"):
        validate_glb(path)
