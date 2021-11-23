# KLIB - variables
# wykys 2021

from pathlib import Path

PATH_KLIB = f'{Path.home()}/projects/klib'
PATH_KICAD = '/usr/share/kicad-nightly'
PATH_KICAD_CONFIG = f'{Path.home()}/.config/kicad/6.0'
PATH_KICAD_COMMON = f'{PATH_KICAD_CONFIG}/kicad_common.json'
PATH_FP_LIB_TABLE = f'{PATH_KICAD_CONFIG}/fp-lib-table'
PATH_SYM_LIB_TABLE = f'{PATH_KICAD_CONFIG}/sym-lib-table'


class KlibVars(object):

    def __init__(self) -> None:
        self.name_symbols = ''
        self.name_models3d = ''
        self.name_footprints = ''

        self.dir_symbols = ''
        self.dir_models3d = ''
        self.dir_footprints = ''

    def set_symbols(self, name: str, value: str) -> None:
        self.name_symbols = name
        self.dir_symbols = value

    def set_models3d(self, name: str, value: str) -> None:
        self.name_models3d = name
        self.dir_models3d = value

    def set_footprints(self, name: str, value: str) -> None:
        self.name_footprints = name
        self.dir_footprints = value

    def __dict__(self) -> dict:

        res = dict()

        if self.name_symbols != '' and self.dir_symbols != '':
            res[self.name_symbols] = self.dir_symbols

        if self.name_models3d != '' and self.dir_models3d != '':
            res[self.name_models3d] = self.dir_models3d

        if self.name_footprints != '' and self.dir_footprints != '':
            res[self.name_footprints] = self.dir_footprints

        return res


KLIB = KlibVars()
KLIB.set_symbols('KLIB_SYMBOL_DIR', f'{PATH_KLIB}/symbols')
KLIB.set_models3d('KLIB_3DMODEL_DIR', f'{PATH_KLIB}/3dmodels')
KLIB.set_footprints('KLIB_FOOTPRINT_DIR', f'{PATH_KLIB}/footprints')

KICAD = KlibVars()
KICAD.set_symbols('KICAD6_SYMBOL_DIR', f'{PATH_KICAD}/footprints')
KICAD.set_models3d('KICAD6_3DMODEL_DIR', f'{PATH_KICAD}/3dmodels')
KICAD.set_footprints('KICAD6_FOOTPRINT_DIR', f'{PATH_KICAD}/footprints')
