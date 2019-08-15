#!/usr/bin/env python3
# wykys
# automation of installation and administration of KLIB in KiCAD
import difflib
import os
import sys

from colorama import Back, Fore, Style

KLIB_PATH = os.path.expanduser('~') + '/projects/klib/'

KICAD_PATH = '/usr/share/kicad/'
PATH_KICAD_COMMON = os.path.expanduser('~') + '/.config/kicad/kicad_common'
PATH_FP_LIB_TABLE = os.path.expanduser('~') + '/.config/kicad/fp-lib-table'
PATH_SYM_LIB_TABLE = os.path.expanduser('~') + '/.config/kicad/sym-lib-table'
if not os.path.isdir(KICAD_PATH):
    KICAD_PATH = KICAD_PATH = '/usr/share/kicad-nightly/'
    PATH_KICAD_COMMON = os.path.expanduser('~') + '/.config/kicadnightly/kicad_common'
    PATH_FP_LIB_TABLE = os.path.expanduser('~') + '/.config/kicadnightly/fp-lib-table'
    PATH_SYM_LIB_TABLE = os.path.expanduser('~') + '/.config/kicadnightly/sym-lib-table'

KLIB = {
    'W3D': KLIB_PATH + 'packages3d',
    'WMOD': KLIB_PATH + 'modules',
    'WSYM': KLIB_PATH + 'library',
    'WSPI': KLIB_PATH + 'spice',
}

KICAD = {
    'KISYSMOD': KICAD_PATH + 'modules',
    'KISYS3DMOD': KICAD_PATH + 'modules/packages3d',
    'KICAD_TEMPLATE_DIR': KICAD_PATH + 'template',
    'KICAD_SYMBOL_DIR': KICAD_PATH + 'library',
}

LIB = '.lib'
MOD = '.pretty'


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
                    color, Style.BRIGHT, tag, Style.NORMAL, func(content), Style.RESET_ALL
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
            '{}{}{}{}{}{}'.format(
                color, Style.BRIGHT, operation, Style.NORMAL, content, Style.RESET_ALL
            ),
            end=''
        )

    def diff_stat_log(tag, color, number):
        info('{}{}{}{} {}'.format(color, Style.BRIGHT, tag, Style.RESET_ALL, number))

    differ = difflib.Differ()
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
            warning('{} was corrupted, created a new empty table'.format(path))
            lib_table_old = ['(sym_lib_table\n', ')\n'] if extension == LIB else ['(fp_lib_table\n', ')\n']

    lib_table_new = [line for line in lib_table_old if not var in line][:-1]
    var = '${{{}}}'.format(var)

    for lib in library:
        lib_table_new.append(
            '  (lib (name {})(type {})(uri {}/{}{})(options "")(descr ""))\n'.format(
                lib,
                'Legacy' if extension == LIB else 'KiCad',
                var,
                lib,
                extension
            )
        )

    lib_table_new.append(')\n')

    with open(path, 'w') as fw:
        fw.writelines(lib_table_new)

    ok('{} is updated'.format(path))
    return (lib_table_old, lib_table_new)


if __name__ == '__main__':
    try:
        kicad_library = get_libraries(KICAD['KICAD_SYMBOL_DIR'], LIB)
        kicad_modules = get_libraries(KICAD['KISYSMOD'], MOD)

        klib_library = get_libraries(KLIB['WSYM'], LIB)
        klib_modules = get_libraries(KLIB['WMOD'], MOD)

        info('update enviroment variables')
        environment_variables(PATH_KICAD_COMMON)

        info('update official kicad library')
        lib_old = lib_table(PATH_SYM_LIB_TABLE, kicad_library, 'KICAD_SYMBOL_DIR', LIB)[0]
        mod_old = lib_table(PATH_FP_LIB_TABLE, kicad_modules, 'KISYSMOD', MOD)[0]

        info('update klib')
        lib_new = lib_table(PATH_SYM_LIB_TABLE, klib_library, 'WSYM', LIB)[1]
        mod_new = lib_table(PATH_FP_LIB_TABLE, klib_modules, 'WMOD', MOD)[1]

        info('diff sym-lib-table')
        diff(lib_old, lib_new)
        info('diff fp-lib-table')
        diff(mod_old, mod_new)

    except NotExist as e:
        error(str(e))
        exit(1)
