#!/usr/bin/env python3
# wykys
# automation of installation and administration of KLIB in KiCAD
import os

KLIB = {
    'W3D': 'packages3d',
    'WMOD': 'modules',
    'WSYM': 'library',
}

path_klib = os.getcwd()
path_kicad_common = os.path.expanduser('~') + '/.config/kicad/kicad_common'
path_fp_lib_table = os.path.expanduser('~') + '/.config/kicad/fp-lib-table'
path_sym_lib_table = os.path.expanduser('~') + '/.config/kicad/sym-lib-table'

klib_library = sorted([f.name[:-4] for f in os.scandir(KLIB['WSYM']) if len(f.name) > 4 and f.name[-4:] == '.lib'])
klib_modules = sorted([f.name[:-7] for f in os.scandir(KLIB['WMOD']) if len(f.name) > 7 and f.name[-7:] == '.pretty'])


def error_path_not_exist(path):
    print('ERROR: file {} not exist'.format(path))
    exit(1)


def environment_variables():
    if not os.path.exists(path_kicad_common):
        error_path_not_exist(path_kicad_common)

    with open(path_kicad_common, 'r') as fr:
        config_old = fr.readlines()

    config_new = [line for line in config_old if not any(key in line for key in KLIB)]

    for key in KLIB:
        config_new.append('{}={}/{}\n'.format(key, path_klib, KLIB[key]))

    with open(path_kicad_common, 'w') as fw:
        fw.writelines(config_new)


def lib_table(path):
    if not os.path.exists(path):
        error_path_not_exist(path)

    with open(path, 'r') as fr:
        lib_table_old = fr.readlines()

    lib_table_new = [line for line in lib_table_old if not 'KLIB' in line][:-1]

    if 'sym-lib-table' in path:
        for lib in klib_library:
            lib_table_new.append(
                '  (lib (name {})(type Legacy)(uri {}/{}.lib)(options "")(descr ""))\n'.format(lib, '${WSYM}', lib)
            )
    else:
        for lib in klib_modules:
            lib_table_new.append(
                '  (lib (name {})(type KiCad)(uri "{}/{}.pretty")(options "")(descr ""))\n'.format(lib, '${WMOD}', lib)
            )

    lib_table_new.append(')\n')

    with open(path, 'w') as fw:
        fw.writelines(lib_table_new)


if __name__ == '__main__':
    environment_variables()
    lib_table(path_sym_lib_table)
    lib_table(path_fp_lib_table)
