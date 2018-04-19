# Wykys's KiCAD Library
__KLIB__ (KiCAD Library) is a toolkit and libraries for hardware development in KiCAD.


## Requires the definition of these constants
File: `~/.config/kicad/kicad_common`
```
WSYM = path_to_klib/library
WMOD = path_to_klib/footprints
W3D  = path_to_klib/packeges3d
```
You can use `install.py`


## Instalation (for Linux)
Requires `python3+`
```bash
git clone git@github.com:wykys/klib.git
cd klib
./install.py
```
### `install.py`
This script automatically sets environment variables and library tables in KiCAD configuration files (updates: `kicad_common`,` sym-lib-table` and `fp-lib-table`). This script searches for all official KiCAD libraries and KLIB files (extensions: `.lib` and` .pretty`), so it can be used to update or manage library tables.

For the correct operation of this script, it's important to run the script from the KLIB root directory!



## Types for users:

- [ ] the variables are used in the following ways: `$(WSYM)/path_to_lib`
- [ ] `$(KIPRJMOD)` is path to current KiCAD project folder


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


## Links

- [ ] KiCad Library Convention [KLC](http://kicad-pcb.org/libraries/klc/)
- [ ] KLC Helper Scripts [kicad-library-utils](https://github.com/kicad/kicad-library-utils)
