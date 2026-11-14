"""Tests for configuration loading and validation."""
import pytest

from engine.core.config import load_json_config


def test_game_config_has_expected_identity():
    config = load_json_config("game.json")
    assert config["title"] == "ASHENVEIL"
    assert config["version"]


def test_graphics_config_has_rgba_background():
    config = load_json_config("graphics.json")
    color = config["background_color"]
    assert len(color) == 4
    assert all(0.0 <= channel <= 1.0 for channel in color)


def test_rejects_path_traversal():
    with pytest.raises(ValueError):
        load_json_config("../LICENSE")


def test_rejects_non_json_filename():
    with pytest.raises(ValueError):
        load_json_config("game.txt")
