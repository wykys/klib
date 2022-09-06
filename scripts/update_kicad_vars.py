#!/usr/bin/env python3
# Automation of variable installation for KLIB
# wykys 2021

import os
import json
from klib_vars import PATH_KICAD_COMMON, KLIB
from klib_print import info, error
from klib_exception import NotExistException, InvalidFileFormatException


def set_klib_variables(path) -> None:
    if not os.path.exists(path):
        raise NotExistException(path)

    with open(path, 'r', encoding='utf-8') as fr:
        config = json.load(fr)

    if 'environment' not in config:
        raise InvalidFileFormatException(path)

    if 'vars' not in config['environment']:
        raise InvalidFileFormatException(path)

    if config['environment']['vars'] is None:
        config['environment']['vars'] = KLIB.__dict__()
    else:
        config['environment']['vars'].update(KLIB.__dict__())

    with open(path, 'w', encoding='utf-8') as fw:
        json.dump(config, fw, ensure_ascii=False, indent=2)


if __name__ == '__main__':

    try:
        set_klib_variables(PATH_KICAD_COMMON)
        info('KiCad\'s variables have been updated')

    except NotExistException as e:
        error(str(e))
        exit(1)

    except InvalidFileFormatException as e:
        error(str(e))
        exit(2)
