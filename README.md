# Wykys's KiCAD Library

## Links

- [ ] KiCad Library Convention [KLC](http://kicad-pcb.org/libraries/klc/)
- [ ] KLC Helper Scripts [kicad-library-utils](https://github.com/kicad/kicad-library-utils)
- [ ] STEP to WRL [freecad-scripts](https://github.com/SchrodingersGat/freecad-scripts)

## Requires the definition of these constants
File: `~/.config/kicad/kicad_common`
```
WSYM = path_to_klib/library
WMOD = path_to_klib/footprints
W3D  = path_to_klib/packeges3d
```
You can use `install.py`

## Types for users:

- [ ] the variables are used in the following ways: `$(WSYM)/path_to_lib`
- [ ] `${KIPRJMOD}` is path to current KiCAD project folder


## [STEP to WRL](https://github.com/SchrodingersGat/freecad-scripts)

```bash
# go to the freecad scripts destination
cd path/freecad-scripts
# run freecad with parameters:
# - step file name
# - step2wrl.FCMacro
# for example
freecad ~/projects/klib/packages3d/KLIB_Connector_Power.3dshapes/Cliff_FC681495.step step2wrl.FCMacro
```
