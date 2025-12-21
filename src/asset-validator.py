import maya.cmds as cmds

def validate_selected_assets():
    selection = cmds.ls(selection=True, long=True)

    if not selection:
        cmds.warning("No objects selected.")
        return

    print("=== Asset Validation Report ===")

    for obj in selection:
        if cmds.nodeType(obj) != "transform":
            continue

        shapes = cmds.listRelatives(obj, shapes=True)
        if not shapes:
            continue

        poly_count = cmds.polyEvaluate(obj, face=True)
        scale = cmds.getAttr(obj + ".scale")[0]
        transforms_frozen = all(abs(s - 1.0) < 0.001 for s in scale)

        print(f"\nAsset: {obj}")
        print(f"  Poly Count: {poly_count}")
        print(f"  Scale: {scale}")
        print(f"  Transforms Frozen: {transforms_frozen}")
        

validate_selected_assets()