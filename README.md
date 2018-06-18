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
cd klib/scripts
make install
```

## Scripts
The KLIB contains scripts for easy work with KiCAD. You can run all the scripts simply through `Makefile`. For the correct operation of this scripts, it's important to __run the script from the `klib/scripts` directory!__

### `help`
Lists basic help.

#### Use:
```bash
make help
```

### `install`
Creates the python environment needed for some scripts. Closes third-party repositories. Install the necessary packages. Configures the KiCAD settings. Requires root rights.

#### Use:
```bash
make install
```

### `update_kicad_settings`
This script automatically sets environment variables and library tables in KiCAD configuration files (updates: `kicad_common`,` sym-lib-table` and `fp-lib-table`). This script searches for all official KiCAD libraries and KLIB files (extensions: `.lib` and` .pretty`), so it can be used to update or manage library tables.

#### Use:
```bash
# the first option is to run the command
make
# the second option is to run the command
make update_kicad_settings
```

### `venv`
If it does, it removes the current Python environment in the next step creating a new environment where it installs the packages that are listed in the `requirements.txt` file.

#### Use:
```bash
make venv
```

### `step_to_wrl`
Converts the STEP file to a WRL file. It uses [FreeCAD](https://www.freecadweb.org/) and [FreeCAD scripts](https://github.com/SchrodingersGat/freecad-scripts).

#### Use:
```bash
make step_to_wrl step=~/N42GK-04.step
```

### `run`
Runs python script in KLIB python environment.

#### Use:
```bash
make run script=~/your_script.py
```


## Types for users:

- [ ] the variables are used in the following ways: `$(WSYM)/path_to_lib`
- [ ] `$(KIPRJMOD)` is path to current KiCAD project folder


## Links

- [ ] KiCad Library Convention [KLC](http://kicad-pcb.org/libraries/klc/)
- [ ] KLC Helper Scripts [kicad-library-utils](https://github.com/kicad/kicad-library-utils)
