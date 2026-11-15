# Testing ASHENVEIL M1.2 — Collision, terrain and camera

This is a source-code development branch, not a packaged installer.

## Get this branch

Download the ZIP from:

https://github.com/lawrenceibeh60-glitch/ASHENVEIL/tree/m1.2/collision-terrain-camera

Or clone it with Git:

```powershell
git clone --branch m1.2/collision-terrain-camera https://github.com/lawrenceibeh60-glitch/ASHENVEIL.git
cd ASHENVEIL
```

## Install and launch

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

## Controls

| Input | Action |
| --- | --- |
| W / A / S / D | Move |
| Space | Jump |
| Mouse | Orbit the third-person camera |
| Esc | Exit |

## M1.2 checks

1. Walk toward either greybox obstacle; the player should stop at its boundary.
2. Move along an obstacle edge; movement should slide along the wall rather than freezing completely.
3. Jump and check that the player can clear obstacles when high enough.
4. Approach the raised platform; it should not be walkable from ground level.
5. Jump onto the raised platform; land on its top if the jump clears the edge.
6. Walk off the platform; the player should fall to the base ground.
7. Rotate the camera near an obstacle; the camera should move closer rather than pass through it.
8. Move toward the arena edge; the player should remain within the world boundary.
9. Press Esc and confirm the game closes cleanly.

## Automated checks

Run:

```powershell
python -m compileall -q engine tools tests main.py
python -m pytest -q
```

The collision and camera geometry helpers are pure Python and have unit tests. These tests do not prove the Panda3D window or mouse behaviour works on every Windows machine.

## Current limitations

- The player is still a temporary box-shaped placeholder.
- Collision uses axis-aligned boxes and rectangular ground surfaces; it is not yet a general terrain mesh collider.
- The raised platform is a test surface, not a production traversal system.
- Camera obstruction checks the configured obstacle boxes; it does not yet handle arbitrary imported mesh geometry.
- Slopes, stairs, moving platforms, character animations and final character assets remain future work.
- A Windows graphical test is still required.
