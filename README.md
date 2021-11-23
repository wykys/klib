# Wykys's KiCad Library

__KLIB__ (KiCad Library) is a toolkit and libraries for hardware development in KiCad.

## Installation for GNU/Linux

Requires `python3+`

```bash
git clone git@gitlab.com:wykys/klib.git
cd klib/scripts
make install
```

## Scripts

The KLIB contains scripts for easy work with KiCad. You can run all the scripts simply through `Makefile`. For the correct operation of this scripts, it's important to __run the script from the `klib/scripts` directory!__

### HELP

Lists basic help.

#### Use:

```bash
make help
```

### INSTALL

Creates the Python environment needed for some scripts. Clones the official KiCad repository with scripts for checking KLC. Configures KiCad settings. The installation will also make the following scripts available on the system:

* `klib-update` - Updates library tables
* `klib-upgrade` - Updates repositories, configurations and scripts
* `klib-check-symbol` - Check KLC schematic symbol
* `klib-check-footprint` - Check KLC footprint

#### Use:

```bash
make install
```

### UPDATE KICAD ENVIROMENT VARS

This script automatically sets the environment variables necessary for the KLIB correct function. Extends the `~/.config/kicad/6.0/kicad_common.json` file with the following variables:

```json
{
  "environment": {
      "vars": {
        "KLIB_SYMBOL_DIR": "path_to_klib/symbols",
        "KLIB_3DMODEL_DIR": "path_to_klib/3dmodels",
        "KLIB_FOOTPRINT_DIR": "path_to_klib/footprints"
      }
    },
}
```

#### Use:

```bash
# the first option is to run the command
make
# the second option is to run the command
make update_kicad_vars
```

### UPDATE KICAD LIB TABLES

This script updates the library tables. It does this by searching for KiCad and KLIB library files (extensions: `.kicad_sym` and `.pretty`) and updating the `sym-lib-table` and `fp-lib-table` files based on data analysis.

```bash
# the first option is to run the command
make update_kicad_lib_tables
# it is equivalent
klib-update
```

### VENV

If it does, it removes the current Python environment in the next step creating a new environment where it installs the packages that are listed in the `requirements.txt` file.

#### Use:

```bash
make venv
```

### STL TO X3D

I use [Blender](https://www.blender.org/) to convert STL to X3D. I have created a Blender API [script](https://github.com/wykys/klib/blob/master/scripts/blender.py) that will make the necessary transformations before exporting to X3D to correctly display the output in KiCad.

### RUN

Runs python script in KLIB python environment.

#### Use:

```bash
make run script=~/your_script.py
```


## Types for users:

* the variables are used in the following ways: `${KLIB_SYMBOL_DIR}/path_to_lib`
* `${KIPRJMOD}` is path to current KiCad project folder


## Links

* KiCad Library Convention [KLC](https://klc.kicad.org/)
* KLC Helper Scripts [KiCad Library utilities](https://gitlab.com/kicad/libraries/kicad-library-utils)
