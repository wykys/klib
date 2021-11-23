#!/usr/bin/env python3
# Automation of generation and updating of lib tables for KiCad v6
# wykys 2021

import os
from glob import glob
from klib_diff import diff
from klib_exception import NotExistException
from klib_print import info, warning, error
from klib_vars import KLIB, KICAD, PATH_SYM_LIB_TABLE, PATH_FP_LIB_TABLE

SYMBOL_LIB = '.kicad_sym'
FOOTPRINT_LIB = '.pretty'


def get_libraries(path, extension):
    if not os.path.exists(path):
        raise NotExistException(path)

    return sorted(
        lib[len(str(path)) + 1: -len(extension)]
        for lib in glob(f'{path}/*{extension}')
    )


def check_lib_table_format(lib_table: list) -> bool:
    if (
        len(lib_table) < 2 or lib_table[-1] != ')\n' or
        'lib_table' not in lib_table[0]
    ):
        return False
    return True


def update_lib_table(path, library, var, extension):
    if not os.path.exists(path):
        fw = open(path, 'w')
        fw.close()

    with open(path, 'r') as fr:
        lib_table_old = fr.readlines()
        if not check_lib_table_format(lib_table_old):
            warning(f'{path} was corrupted, created a new empty table')
            if extension == SYMBOL_LIB:
                lib_table_old = ['(sym_lib_table\n', ')\n']
            else:
                lib_table_old = ['(fp_lib_table\n', ')\n']

    lib_table_new = [line for line in lib_table_old[:-1] if var not in line]

    for lib in library:
        lib_table_new.append(
            f'  (lib '
            f'(name {lib})(type KiCad)'
            f'(uri ${{{var}}}/{lib}{extension})'
            f'(options "")'
            f'(descr "")'
            f')\n'
        )

    lib_table_new.append(')\n')

    with open(path, 'w') as fw:
        fw.writelines(lib_table_new)

    return {
        'old': lib_table_old,
        'new': lib_table_new
    }


if __name__ == '__main__':
    try:
        klib_symbols = get_libraries(KLIB.dir_symbols, SYMBOL_LIB)
        klib_footprints = get_libraries(KLIB.dir_footprints, FOOTPRINT_LIB)

        kicad_symbols = get_libraries(KICAD.dir_symbols, SYMBOL_LIB)
        kicad_footprints = get_libraries(KICAD.dir_footprints, FOOTPRINT_LIB)

        info('Update official symbols KiCad library')
        sym_lib_table_old = update_lib_table(
            PATH_SYM_LIB_TABLE,
            kicad_symbols,
            KICAD.name_symbols,
            SYMBOL_LIB
        )['old']

        info('Update symbols KLIB library')
        sym_lib_table_new = update_lib_table(
            PATH_SYM_LIB_TABLE,
            klib_symbols,
            KLIB.name_symbols,
            SYMBOL_LIB
        )['new']

        info('Update official footprints KiCad library')
        fp_lib_table_old = update_lib_table(
            PATH_FP_LIB_TABLE,
            kicad_footprints,
            KICAD.name_footprints,
            FOOTPRINT_LIB
        )['old']

        info('Update footprints KLIB library')
        fp_lib_table_new = update_lib_table(
            PATH_FP_LIB_TABLE,
            klib_footprints,
            KLIB.name_footprints,
            FOOTPRINT_LIB
        )['new']

        info('Diff sym-lib-table')
        diff(sym_lib_table_old, sym_lib_table_new)
        info('Diff fp-lib-table')
        diff(fp_lib_table_old, fp_lib_table_new)

    except NotExistException as e:
        error(str(e))
        exit(1)
