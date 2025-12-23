import maya.cmds as cmds

WINDOW_NAME = "assetValidatorUI"

def validate_selected_assets_ui(output_field):
    selection = cmds.ls(selection=True, long=True)

    if not selection:
        cmds.scrollField(output_field, edit=True, text="No objects selected.")
        return

    report_lines = []
    report_lines.append("=== Asset Validation Report ===\n")

    for obj in selection:
        if cmds.nodeType(obj) != "transform":
            continue

        shapes = cmds.listRelatives(obj, shapes=True)
        if not shapes:
            continue

        poly_count = cmds.polyEvaluate(obj, face=True)
        scale = cmds.getAttr(obj + ".scale")[0]

        transforms_frozen = (
            abs(scale[0] - 1.0) < 0.001 and
            abs(scale[1] - 1.0) < 0.001 and
            abs(scale[2] - 1.0) < 0.001
        )

        report_lines.append("Asset: " + obj)
        report_lines.append("  Poly Count: " + str(poly_count))
        report_lines.append("  Scale: " + str(scale))
        report_lines.append(
            "  Transforms Frozen: " +
            ("Yes" if transforms_frozen else "No")
        )
        report_lines.append("")

    cmds.scrollField(
        output_field,
        edit=True,
        text="\n".join(report_lines)
    )


def show_ui():
    if cmds.window(WINDOW_NAME, exists=True):
        cmds.deleteUI(WINDOW_NAME)

    window = cmds.window(
        WINDOW_NAME,
        title="Game Asset Validator",
        widthHeight=(400, 300),
        sizeable=False
    )


    cmds.columnLayout(adjustableColumn=True, rowSpacing=10)

    cmds.text(
        label="Validate selected assets for common game-ready issues.",
        align="left"
    )

    output_field = cmds.scrollField(
        editable=False,
        wordWrap=True,
        height=180
    )

    cmds.button(
        label="Validate Selected Assets",
        height=35,
        command=lambda x: validate_selected_assets_ui(output_field)
    )

    cmds.showWindow(window)
