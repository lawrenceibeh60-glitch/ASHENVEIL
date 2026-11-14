# Testing ASHENVEIL on Windows

This guide is for testing the current M1 development build. It is not a packaged installer yet.

## Requirements

- Windows 10 or Windows 11, 64-bit.
- Python 3.11 or newer.
- A keyboard and mouse.
- Internet access for the first dependency installation.

## Get the M1 branch

1. Open https://github.com/lawrenceibeh60-glitch/ASHENVEIL/tree/m1/player-foundation
2. Use **Code → Download ZIP**.
3. Extract the ZIP to a folder such as `C:\Games\ASHENVEIL-M1`.
4. Open PowerShell in that extracted folder.

Alternatively, with Git installed:

```powershell
git clone --branch m1/player-foundation https://github.com/lawrenceibeh60-glitch/ASHENVEIL.git
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

If PowerShell blocks virtual-environment activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python main.py
```

## Current controls

| Input | Action |
| --- | --- |
| W / A / S / D | Move |
| Space | Jump |
| Mouse | Orbit the follow camera |
| Esc | Exit |

The player is currently represented by a simple box-shaped placeholder. This is an engineering test scene, not the finished character or final game.

## What to test

1. Confirm the game window opens without a Python traceback.
2. Walk in all four directions.
3. Move diagonally and check that diagonal movement is not faster.
4. Rotate the camera and confirm movement follows the camera's orientation.
5. Jump while standing still and while moving.
6. Check that the player returns to the ground after jumping.
7. Walk around the greybox obstacles and check for unexpected clipping.
8. Move toward the arena edges and confirm the player stays within the test area.
9. Press Esc and confirm the game closes cleanly.

## Report a problem

If something fails, send:
- A screenshot or short recording of the game window.
- The complete error text from PowerShell, if one appears.
- Your Windows version and Python version.

Do not send passwords, API keys, or other secrets.

## Current limitations

- This is a source-code development build; there is no installer or APK yet.
- The primitive player has no final animations or character model.
- Collision handling, uneven terrain, and camera obstruction are still being developed.
- A successful automated test run does not prove the graphical build works on every Windows PC.
