# create and install python enviroment
# wykys 2018

PYTHON = python3

PIP = pip
PIP_FRERZE = $(PIP) freeze
PIP_UPGRADE = $(PIP) install --upgrade pip
PIP_INSTALL = $(PIP) install -r requirements.txt

VENV = .venv
VENV_CREATE = $(PYTHON) -m venv $(VENV)
VENV_ACTIVATE = . .venv/bin/activate

all: update_kicad_settings

.ONESHELL:
$(VENV):
	$(VENV_CREATE)
	$(VENV_ACTIVATE)
	$(PIP_UPGRADE)
	$(PIP_INSTALL)
	$(PIP_FRERZE)

venv:
	rm -rf $(VENV)
	make $(VENV)

.ONESHELL:
update_kicad_settings: $(VENV)
	$(VENV_ACTIVATE)
	./update_kicad_settings.py

.ONESHELL:
install: $(VENV) update_kicad_settings
	git clone git@github.com:KiCad/kicad-library-utils.git
	PWD=pwd

	echo "#!/usr/bin/env bash" > klib-update.sh
	echo "cd $(PWD)" >> klib-update.sh
	echo "make update_kicad_settings" >> klib-update.sh
	chmod +x klib-update.sh

	cd ~/.local/bin
	ln -s $(PWD)/kicad-library-utils/schlib/checklib.py klib-checklib
	ln -s $(PWD)/kicad-library-utils/pcb/check_kicad_mod.py klib-checkmod
	ln -s $(PWD)/klib-update.sh klib-update

.ONESHELL:
step_to_wrl:
	cd freecad-scripts
	freecad $(step) step2wrl.FCMacro

.ONESHELL:
run: $(VENV)
	$(VENV_ACTIVATE)
	./$(script)

help:
	@echo "KLIB HELP:"
	@echo ""
	@echo "created or upgrade python enviroment:"
	@echo "    make venv"
	@echo ""
	@echo "install KLIB:"
	@echo "    make install"
	@echo ""
	@echo "update KiCAD settings:"
	@echo "    make update_kicad_settings or make"
	@echo ""
	@echo "STEP to WRL:"
	@echo "    make step_to_wrl step=your_step_file.step"
	@echo ""
	@echo "run script in KLIB python enviroment:"
	@echo "    make run script=your_script.py"
	@echo ""
