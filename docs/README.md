# Maya Asset Validator

A Python-based asset validation tool for Maya that helps artists prepare
game-ready assets by automatically checking common technical requirements.

## Problem
In game production, assets often fail technical requirements such as:
- Incorrect naming conventions
- Non-frozen transforms
- Inconsistent scale
- Excessive poly counts

These issues slow down pipelines and cause downstream problems in game engines.

## Solution
This tool allows artists or technical artists to quickly validate selected assets
inside Maya and receive immediate feedback on common technical issues.

## Features
- Poly count reporting
- Transform and scale validation
- Supports batch validation
- Lightweight and easy to extend

## Requirements
- Autodesk Maya 2020+
- Python (maya.cmds)

## Usage
1. Open Maya
2. Open the Script Editor (Python tab)
3. Load `asset_validator.py`
4. Select one or more meshes
5. Run `validate_selected_assets()`

## Future Improvements
- UI-based workflow
- Automatic fixes
- FBX export presets
- Unity / Unreal integration
