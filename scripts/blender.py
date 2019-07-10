# script to prepare data for export from stl to x3d using blender
# wykys 2019
#
# Readme:
#  Start Blender and import stl files into it.
#  Then open the Scripting tab and load this script (Alt + O).
#  The script (Alt + P) starts.
#  The result is suitable for export to x3d and use in KiCAD.
#
# Notes:
#  Tested in Blender v2.79
#  The unit in the STL input files was mm.

import bpy
from math import pi

# select all
bpy.ops.object.select_all(action='SELECT')

# resize from mm to mils
mm_to_mils = 1/2.54
bpy.ops.transform.resize(
    value=(mm_to_mils, mm_to_mils, mm_to_mils),
    constraint_axis=(False, False, False),
    constraint_orientation='GLOBAL',
    mirror=False,
    proportional='DISABLED',
    proportional_edit_falloff='SMOOTH',
    proportional_size=1
)

# x rototation -pi
bpy.ops.transform.rotate(
    value=-pi/2,
    axis=(1, 0, 0),
    constraint_axis=(True, False, False),
    constraint_orientation='GLOBAL',
    mirror=False,
    proportional='DISABLED',
    proportional_edit_falloff='SMOOTH',
    proportional_size=1
)

# y rototation 2 * pi
bpy.ops.transform.rotate(
    value=pi,
    axis=(0, 1, 0),
    constraint_axis=(False, True, False),
    constraint_orientation='GLOBAL',
    mirror=False,
    proportional='DISABLED',
    proportional_edit_falloff='SMOOTH',
    proportional_size=1
)
