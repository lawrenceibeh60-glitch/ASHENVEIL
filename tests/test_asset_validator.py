"""Tests for the first asset inventory utility."""
from pathlib import Path

from tools.asset_validator import inspect_assets


def test_asset_inventory_finds_glb(tmp_path: Path):
    (tmp_path / "hero.glb").write_bytes(b"placeholder")
    (tmp_path / "readme.txt").write_text("asset note", encoding="utf-8")

    report = inspect_assets(tmp_path)
    assert report["file_count"] == 2
    assert report["model_count"] == 1
    assert report["models"] == ["hero.glb"]


def test_asset_inventory_reports_unsupported_source(tmp_path: Path):
    (tmp_path / "source.blend").write_bytes(b"not a real blend file")

    report = inspect_assets(tmp_path)
    assert report["unsupported_source_files"] == ["source.blend"]
