#!/usr/bin/env python3
# wykys
# automation of installation and administration of KLIB in KiCAD
import os
import sys

from colorama import Back, Fore, Style

KLIB = {
    'W3D': 'packages3d',
    'WMOD': 'modules',
    'WSYM': 'library',
}

LIB = '.lib'
MOD = '.pretty'

path_klib = os.getcwd()
path_kicad_common = os.path.expanduser('~') + '/.config/kicad/kicad_common'
path_fp_lib_table = os.path.expanduser('~') + '/.config/kicad/fp-lib-table'
path_sym_lib_table = os.path.expanduser('~') + '/.config/kicad/sym-lib-table'

klib_library = sorted([f.name[:-len(LIB)] for f in os.scandir(KLIB['WSYM'])
                       if len(f.name) > len(LIB) and f.name[-len(LIB):] == LIB])
klib_modules = sorted([f.name[:-len(MOD)] for f in os.scandir(KLIB['WMOD'])
                       if len(f.name) > len(MOD) and f.name[-len(MOD):] == MOD])


def error(text):
    print('{}{}ERROR:{} {}{}'.format(Fore.RED, Style.BRIGHT, Style.NORMAL, text, Style.RESET_ALL), file=sys.stderr)
    exit(1)


def ok(text):
    print('{}{}OK:{} {}{}'.format(Fore.GREEN, Style.BRIGHT, Style.NORMAL, text, Style.RESET_ALL), file=sys.stdout)


def environment_variables(path):
    if not os.path.exists(path):
        error('file {} does not exist'.format(path))

    with open(path, 'r') as fr:
        config_old = fr.readlines()

    config_new = [line for line in config_old if not any(key in line for key in KLIB)]

    for key in KLIB:
        config_new.append('{}={}/{}\n'.format(key, path_klib, KLIB[key]))

    with open(path, 'w') as fw:
        fw.writelines(config_new)

    ok('{} is updated'.format(path))


def lib_table(path):
    if not os.path.exists(path):
        error('file {} does not exist'.format(path))

    with open(path, 'r') as fr:
        lib_table_old = fr.readlines()

    lib_table_new = [line for line in lib_table_old if not 'KLIB' in line][:-1]

    if 'sym-lib-table' in path:
        for lib in klib_library:
            lib_table_new.append(
                '  (lib (name {})(type Legacy)(uri {}/{}{})(options "")(descr ""))\n'.format(lib, '${WSYM}', lib, LIB)
            )
    else:
        for lib in klib_modules:
            lib_table_new.append(
                '  (lib (name {})(type KiCad)(uri "{}/{}{}")(options "")(descr ""))\n'.format(lib, '${WMOD}', lib, MOD)
            )

    lib_table_new.append(')\n')

    with open(path, 'w') as fw:
        fw.writelines(lib_table_new)

    ok('{} is updated'.format(path))


if __name__ == '__main__':
    environment_variables(path_kicad_common)
    lib_table(path_sym_lib_table)
    lib_table(path_fp_lib_table)
