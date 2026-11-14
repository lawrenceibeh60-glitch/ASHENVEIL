"""Validated loading for project JSON configuration."""
import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "config"


def load_json_config(filename: str) -> dict[str, Any]:
    """Load a JSON object from the project's config directory."""
    if Path(filename).name != filename or not filename.endswith(".json"):
        raise ValueError("Config filename must be a simple .json filename.")

    path = CONFIG_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    with path.open("r", encoding="utf-8") as config_file:
        data = json.load(config_file)

    if not isinstance(data, dict):
        raise ValueError(f"Configuration root must be a JSON object: {filename}")

    return data
