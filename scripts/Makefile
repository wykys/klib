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

all: set_venv

.ONESHELL:
$(VENV):
	$(VENV_CREATE)
	$(VENV_ACTIVATE)
	$(PIP_UPGRADE)
	$(PIP_INSTALL)
	$(PIP_FRERZE)

upgrade_venv:
	rm -rf $(VENV)
	make $(VENV)

.ONESHELL:
update_kicad_settings: $(VENV)
	$(VENV_ACTIVATE)
	./update_kicad_settings.py

.ONESHELL:
run: $(VENV)
	$(VENV_ACTIVATE)
	./$(script)

help:
	@echo "run script=your_script.py"
