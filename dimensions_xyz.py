import maya.cmds as cmds


def get_object_bounding_box_size():
  # Get the currently selected objects
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
