"""Safe, small wrapper around Panda3D's registered model loaders."""
from pathlib import Path

from panda3d.core import NodePath

from engine.core.config import PROJECT_ROOT

MODEL_SUFFIXES = {".glb", ".gltf", ".bam", ".egg", ".obj"}


def load_model(loader, asset_path: str | Path) -> NodePath:
    """Load a supported model from the repository or an absolute path.

    The panda3d-gltf package supplies glTF support to Panda3D's model loader.
    This wrapper validates the path and extension before handing it to Panda3D.
    """
    path = Path(asset_path)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    path = path.resolve()

    if path.suffix.lower() not in MODEL_SUFFIXES:
        raise ValueError(f"Unsupported model format: {path.suffix}")
    if not path.is_file():
        raise FileNotFoundError(f"Model asset not found: {path}")

    model = loader.loadModel(str(path))
    if model is None or model.isEmpty():
        raise RuntimeError(f"Panda3D could not load model: {path}")
    return model
