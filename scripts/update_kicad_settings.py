#!/usr/bin/env python3
# wykys
# automation of installation and administration of KLIB in KiCAD

import os
import sys

from difflib import Differ
from colorama import Fore, Style

KLIB_PATH = os.path.expanduser('~') + '/projects/klib'

KICAD_PATH = '/usr/share/kicad-nightly'
PATH_KICAD_CONFIG = os.path.expanduser('~') + '/.config/kicad/6.0'
PATH_FP_LIB_TABLE = f'{PATH_KICAD_CONFIG}/fp-lib-table'
PATH_SYM_LIB_TABLE = f'{PATH_KICAD_CONFIG}/sym-lib-table'

KLIB = {
    'KLIB_SYMBOL_DIR': f'{KLIB_PATH}/symbols',
    'KLIB_3DMODEL_DIR': f'{KLIB_PATH}/3dmodels',
    'KLIB_FOOTPRINT_DIR': f'{KLIB_PATH}/footprints'
}

KICAD = {
    'KICAD6_FOOTPRINT_DIR': f'{KICAD_PATH}/footprints',
    'KICAD6_SYMBOL_DIR': f'{KICAD_PATH}/symbols'
}

SYMBOL_LIB = '.kicad_sym'
FOOTPRINT_LIB = '.pretty'


class NotExist(Exception):
    def __init__(self, name):
        self.error_text = '{} is not exist'.format(name)

    def __str__(self):
        return self.error_text


def log(tag, color, fil):
    def log_decorator(func):
        def func_wrapper(content):
            print(
                '{}{}{}:{} {}{}'.format(
                    color, Style.BRIGHT, tag, Style.NORMAL, func(
                        content), Style.RESET_ALL
                ),
                file=fil
            )
        return func_wrapper
    return log_decorator


@log('ERROR', Fore.RED, sys.stderr)
def error(content):
    return content


@log('WARNING', Fore.YELLOW, sys.stderr)
def warning(content):
    return content


@log('OK', Fore.GREEN, sys.stdout)
def ok(content):
    return content


@log('INFO', Fore.WHITE, sys.stdout)
def info(content):
    return content


def get_libraries(path, extension):
    if not os.path.exists(path):
        raise NotExist(path)

    ext_len = len(extension)
    return sorted(
        f.name[:-ext_len] for f in os.scandir(path) if all((
            len(f.name) > ext_len,
            f.name[-ext_len:] == extension
        ))
    )


def diff(text1_lines, text2_lines):
    def diff_change_log(color, operation, content):
        print(
            f'{color}{Style.BRIGHT}{operation}{Style.NORMAL}{content}{Style.RESET_ALL}',
            end='',
        )

    def diff_stat_log(tag, color, number):
        info(f'{color}{Style.BRIGHT}{tag}{Style.RESET_ALL} {number}')

    differ = Differ()
    added_lines = 0
    removed_lines = 0

    for line in differ.compare(text1_lines, text2_lines):
        if line[0] == '+':
            added_lines += 1
            diff_change_log(Fore.GREEN, '+', line[1:])

        elif line[0] == '-':
            diff_change_log(Fore.RED, '-', line[1:])
            removed_lines += 1

    if added_lines > 0 or removed_lines > 0:
        info('change statistics')
        diff_stat_log('+++', Fore.GREEN, added_lines)
        diff_stat_log('---', Fore.RED, removed_lines)


def environment_variables(path):
    if not os.path.exists(path):
        raise NotExist(path)

    with open(path, 'r') as fr:
        config_old = fr.readlines()

    config_new = [
        line for line in config_old if not any((
            any(key in line for key in KICAD),
            any(key in line for key in KLIB)
        ))
    ]

    for key in sorted([key for key in KICAD]):
        config_new.append('{}={}\n'.format(key, KICAD[key]))

    for key in sorted([key for key in KLIB]):
        config_new.append('{}={}\n'.format(key, KLIB[key]))

    diff(config_old, config_new)

    with open(path, 'w') as fw:
        fw.writelines(config_new)

    ok('{} is updated'.format(path))


def lib_table(path, library, var, extension):
    if not os.path.exists(path):
        fw = open(path, 'w')
        fw.close()

    with open(path, 'r') as fr:
        lib_table_old = fr.readlines()
        if len(lib_table_old) < 2 or lib_table_old[-1] != ')\n' or not 'lib_table' in lib_table_old[0]:

            warning(f'{path} was corrupted, created a new empty table')

            if extension == SYMBOL_LIB:
                lib_table_old = ['(sym_lib_table\n', ')\n']
            else:
                lib_table_old = ['(fp_lib_table\n', ')\n']

    lib_table_new = [line for line in lib_table_old if not var in line][:-1]
    var = f'${{{var}}}'

    for lib in library:
        lib_table_new.append(
            f'  (lib (name {lib})(type KiCad)(uri {var}/{lib}{extension})(options "")(descr ""))\n'
        )

    lib_table_new.append(')\n')

    with open(path, 'w') as fw:
        fw.writelines(lib_table_new)

    ok('{} is updated'.format(path))
    return (lib_table_old, lib_table_new)


if __name__ == '__main__':
    try:
        kicad_symbols = get_libraries(KICAD['KICAD6_SYMBOL_DIR'], SYMBOL_LIB)
        kicad_footprints = get_libraries(
            KICAD['KICAD6_FOOTPRINT_DIR'], FOOTPRINT_LIB)

        klib_symbols = get_libraries(KLIB['KLIB_SYMBOL_DIR'], SYMBOL_LIB)
        klib_footprints = get_libraries(
            KLIB['KLIB_FOOTPRINT_DIR'], FOOTPRINT_LIB)

        #info('update enviroment variables')
        # environment_variables(PATH_KICAD_COMMON)

        info('update official kicad library')
        lib_old = lib_table(PATH_SYM_LIB_TABLE, kicad_symbols,
                            'KICAD6_SYMBOL_DIR', SYMBOL_LIB)[0]
        mod_old = lib_table(PATH_FP_LIB_TABLE,
                            kicad_footprints, 'KICAD6_FOOTPRINT_DIR', FOOTPRINT_LIB)[0]

        info('update klib')
        lib_new = lib_table(PATH_SYM_LIB_TABLE, klib_symbols, 'KLIB_SYMBOL_DIR', SYMBOL_LIB)[1]
        mod_new = lib_table(PATH_FP_LIB_TABLE, klib_footprints, 'KLIB_FOOTPRINT_DIR', FOOTPRINT_LIB)[1]

        info('diff sym-lib-table')
        diff(lib_old, lib_new)
        info('diff fp-lib-table')
        diff(mod_old, mod_new)

    except NotExist as e:
        error(str(e))
        exit(1)
