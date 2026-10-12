# Dimensions XYZ

## Overview

**Dimensions XYZ** is a lightweight Autodesk Maya Python utility designed for technical artists, modellers, and riggers. It calculates and outputs the exact world-space dimensions (width, height, and depth) based on the bounding box of any selected mesh or object directly to the Script Editor.

## Tooltip & Shelf Details

* **Label / Name:** `BBox` or `DimXYZ`or `Dimensions XYZ`
* **Tooltip:**
  > Calculates width, height, and depth across world axes for selected mesh.

## Features

* **Accurate World-Space Calculation:** Queries exact bounding box coordinates using Maya's native commands (`cmds.exactWorldBoundingBox`).
* **Multi-Object Support:** Quickly inspects multiple selected objects in succession.
* **Clean Formatting:** Prints formatted results with 4-decimal precision for precise unit verification.

## Python Script

```
import maya.cmds as cmds


def get_object_bounding_box_size():
  # Get currently selected objects in the scene
  selection = cmds.ls(selection=True)

  if not selection:
    print(
        "No object selected. Please select an object in the viewport or"
        " Outliner."
    )
    return

  for obj in selection:
    # exactWorldBoundingBox returns [xmin, ymin, zmin, xmax, ymax, zmax]
    bbox = cmds.exactWorldBoundingBox(obj)

    # Calculate the size for each axis
    size_x = bbox[3] - bbox[0]
    size_y = bbox[4] - bbox[1]
    size_z = bbox[5] - bbox[2]

    # Print the results to the Script Editor
    print(f"--- Bounding Box Sizes for: {obj} ---")
    print(f"  X Size (Width):  {size_x:.4f}")
    print(f"  Y Size (Height): {size_y:.4f}")
    print(f"  Z Size (Depth):  {size_z:.4f}")


# Run the function
get_object_bounding_box_size()

```

## Installation & Usage

1. Open Autodesk Maya.
2. Open the **Script Editor** (`Windows > General Editors > Script Editor`).
3. Switch to the **Python** tab.
4. Copy and paste the code above into the editor.
5. Select any mesh in your viewport and execute the script o view its exact dimensions.
6. *(Optional)* Highlight the code, middle-mouse drag it to your custom Maya shelf to create a quick-access button.
7. *(Optional)* Set the button icon to `icons/icon_dimxyz.png`.
