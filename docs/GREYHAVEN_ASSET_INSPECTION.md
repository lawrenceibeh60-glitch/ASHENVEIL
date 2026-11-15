# Greyhaven building pack — inspection report

## Source asset

- Release: [ASHENVEIL Greyhaven Assets v1](https://github.com/lawrenceibeh60-glitch/ASHENVEIL/releases/tag/greyhaven-assets-v1)
- File: `building_pack_free_low-poly_3d_model_in_fbx.glb`
- Size: 31,936,184 bytes
- Format: binary glTF 2.0
- Meshes: 9
- Materials: 9
- Embedded PNG images: 9
- External texture files: none referenced

## What the visual inspection shows

A geometry preview of the complete GLB shows a compact showcase arrangement of medieval buildings, including several timber/stone house forms and a windmill-like structure. The models are laid out together in one scene rather than supplied as nine separately named, ready-to-place building files.

The GLB's node and mesh names are mostly exporter-generated names such as `Cube.001` and `Cube.003`. They do not reliably identify the individual structures. The nine mesh objects therefore must not be treated as nine separate houses without further inspection.

## Integration decision

Keep this asset as a separate environment preview until it has been inspected in the actual Panda3D runtime. Do not create final per-building collision boxes from the mesh count alone. The asset can be loaded as a complete group for visual evaluation, but its layout, ground contact, orientation, scale, and texture rendering need to be confirmed in Panda3D before it becomes part of the playable Greyhaven scene.

The standalone preview tool automatically reads the imported model bounds and frames the camera around the asset. It does not replace the M1.2 player test scene.

## Texture and performance notes

All nine PNG textures are embedded in the GLB. Their source dimensions are either 1024x1024 or 2048x1024. The current file is about 31.9 MB, so it should be profiled on the target Windows PC before being treated as a final runtime asset. A reduced-resolution copy may be appropriate for low-memory systems, but the original release asset remains unchanged.

## Verification status

- GLB header, version, declared length, scene nodes, mesh count, materials, and embedded image references: inspected.
- Geometry silhouette and overall showcase arrangement: inspected with an independent GLB-capable renderer.
- Panda3D model loading, material/texture fidelity, camera framing in Panda3D, and Windows runtime performance: pending a graphical Panda3D run.
- Final world placement and per-structure collision boundaries: pending that runtime inspection.

## Local preview

From the repository root:

```powershell
python tools/install_greyhaven_assets.py
python tools/preview_greyhaven_assets.py
```

Press Escape to close the preview.
