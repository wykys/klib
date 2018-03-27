#!/usr/bin/env python3
# wykys
# automatically add KiCAD environment variables necessary for the KLIB
import os

KLIB = {
    'W3D': 'packages3d',
    'WMOD': 'modules',
    'WSYM': 'library',
}

path_config = os.path.expanduser('~') + '/.config/kicad/kicad_common'
path_klib = os.getcwd()

if os.path.exists(path_config) == False:
    print('ERROR: file {} not exist'.format(path_config))
    exit(1)

with open(path_config, 'r') as fr:
    config_old = fr.readlines()

config_new = [line for line in config_old if not any(key in line for key in KLIB)]

for key in KLIB:
    config_new.append('{}={}/{}\n'.format(key, path_klib, KLIB[key]))

with open(path_config, 'w') as fw:
    fw.writelines(config_new)
