# Wykys's KiCad Library

__KLIB__ (KiCad Library) is a toolkit and libraries for hardware development in KiCad.

## Requires the definition of these paths

File: `~/.config/kicad/6.0/kicad_common.json`

```json
{
  // ...
  "environment": {
      "vars": {
        "KLIB_SYMBOL_DIR": "path_to_klib/symbols",
        "KLIB_3DMODEL_DIR": "path_to_klib/3dmodels",
        "KLIB_FOOTPRINT_DIR": "path_to_klib/footprints"
      }
    },
  // ...
}
```

## Installation for GNU/Linux

Requires `python3+`

```bash
git clone git@gitlab.com:wykys/klib.git
cd klib/scripts
make install
```

## Scripts

The KLIB contains scripts for easy work with KiCAD. You can run all the scripts simply through `Makefile`. For the correct operation of this scripts, it's important to __run the script from the `klib/scripts` directory!__

### HELP

Lists basic help.

#### Use:

```bash
make help
```

### INSTALL

Creates the python environment needed for some scripts. Closes third-party repositories. Install the necessary packages. Configures the KiCAD settings. Requires root rights. It also creates `klib-chacklib` and `klib-checkmod` links for KLC testing.

#### Use:

```bash
make install
```

### UPDATE KICAD SETTINGS

This script automatically sets environment variables and library tables in KiCAD configuration files (updates: `kicad_common`,` sym-lib-table` and `fp-lib-table`). This script searches for all official KiCAD libraries and KLIB files (extensions: `.lib` and` .pretty`), so it can be used to update or manage library tables.

#### Use:

```bash
# the first option is to run the command
make
# the second option is to run the command
make update_kicad_settings
```

### VENV

If it does, it removes the current Python environment in the next step creating a new environment where it installs the packages that are listed in the `requirements.txt` file.

#### Use:

```bash
make venv
```

### STL TO X3D

I use [Blender](https://www.blender.org/) to convert STL to X3D. I have created a Blender API [script](https://github.com/wykys/klib/blob/master/scripts/blender.py) that will make the necessary transformations before exporting to X3D to correctly display the output in KiCAD.

### STEP TO WRL

Converts the STEP file to a WRL file. It uses [FreeCAD](https://www.freecadweb.org/) and [FreeCAD scripts](https://github.com/SchrodingersGat/freecad-scripts).

#### Use:

```bash
make step_to_wrl step=~/N42GK-04.step
```

### RUN

Runs python script in KLIB python environment.

#### Use:

```bash
make run script=~/your_script.py
```


## Types for users:

* the variables are used in the following ways: `$(KLIB_SYMBOL_DIR)/path_to_lib`
* `$(KIPRJMOD)` is path to current KiCad project folder


## Links

* KiCad Library Convention [KLC](https://klc.kicad.org/)
* KLC Helper Scripts [KiCad Library utilities](https://gitlab.com/kicad/libraries/kicad-library-utils)
