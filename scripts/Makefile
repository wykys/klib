# KLIB Makefile
# - simplifies the creation of python venv
# - allows you to install and easily update libraries
# wykys 2018 - 2021

PYTHON = python3

PIP = pip3
PIP_FRERZE = $(PIP) freeze
PIP_UPGRADE = $(PIP) install --upgrade pip
PIP_INSTALL = $(PIP) install -r requirements.txt

VENV = .venv
VENV_CREATE = $(PYTHON) -m venv $(VENV)
VENV_ACTIVATE = . .venv/bin/activate

all: update_kicad_lib_tables

.ONESHELL:
$(VENV):
	@$(VENV_CREATE)
	@$(VENV_ACTIVATE)
	@$(PIP_UPGRADE)
	@$(PIP_INSTALL)
	@$(PIP_FRERZE)

venv:
	@rm -rf $(VENV)
	@make $(VENV)

.ONESHELL:
update_kicad_vars: $(VENV)
	@$(VENV_ACTIVATE)
	@./update_kicad_vars.py

.ONESHELL:
update_kicad_lib_tables: $(VENV)
	@$(VENV_ACTIVATE)
	@./update_kicad_lib_tables.py

.ONESHELL:
install: $(VENV) update_kicad_vars
	@git clone https://gitlab.com/kicad/libraries/kicad-library-utils.git
	@PWD=pwd

	@echo "#!/usr/bin/env bash" > klib-update.sh
	@echo "cd $(PWD)" >> klib-update.sh
	@echo "make update_kicad_lib_tables" >> klib-update.sh
	@chmod +x klib-update.sh

	@echo "#!/usr/bin/env bash" > klib-upgrade.sh
	@echo "cd $(PWD)" >> klib-upgrade.sh
	@echo "git reset --hard HEAD" >> klib-upgrade.sh
	@echo "git pull" >> klib-upgrade.sh
	@echo "cd kicad-library-utils" >> klib-upgrade.sh
	@echo "git reset --hard HEAD" >> klib-upgrade.sh
	@echo "git pull" >> klib-upgrade.sh
	@echo "cd .." >> klib-upgrade.sh
	@echo "make update_kicad_vars" >> klib-upgrade.sh
	@echo "make update_kicad_lib_tables" >> klib-upgrade.sh
	@echo "make install" >> klib-upgrade.sh
	@chmod +x klib-upgrade.sh

	@cd ~/.local/bin
	@rm -rf klib-*
	@ln -s $(PWD)/kicad-library-utils/klc-check/check_symbol.py klib-check-symbol
	@ln -s $(PWD)/kicad-library-utils/klc-check/check_footprint.py klib-check-footprint
	@ln -s $(PWD)/klib-update.sh klib-update
	@ln -s $(PWD)/klib-upgrade.sh klib-upgrade

.ONESHELL:
step_to_wrl:
	@cd freecad-scripts
	@freecad $(step) step2wrl.FCMacro

.ONESHELL:
run: $(VENV)
	@$(VENV_ACTIVATE)
	@./$(script)

help:
	@echo "KLIB help:"
	@echo ""
	@echo "created or upgrade python enviroment:"
	@echo "    make venv"
	@echo ""
	@echo "install KLIB:"
	@echo "    make install"
	@echo ""
	@echo "update KiCad variables in kicad_common.json:"
	@echo "    make update_kicad_vars"
	@echo "update KiCad lib tables:"
	@echo "    make update_kicad_lib_tables or make"
	@echo ""
	@echo "STEP to WRL:"
	@echo "    make step_to_wrl step=your_step_file.step"
	@echo ""
	@echo "run script in KLIB python enviroment:"
	@echo "    make run script=your_script.py"
	@echo ""
