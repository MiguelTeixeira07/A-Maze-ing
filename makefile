SHELL := /bin/bash

MAIN = a_maze_ing.py
CONFIG_FILE = default_config.txt

EXECUTE = python3
MUTE = > /dev/null

PIP = -m pip install

VENV = -m venv venv

FLAKE = -m flake8 .

MYPY = -m mypy .
MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
STRICT = --strict

DEBUG = -m pdb

FIND = find .
PYCACHE = -type d -name '__pycache__'
MYPY_CACHE = -type d -name '.mypy_cache'
VENV_DIR = -type d -name 'venv'
TXT = -type f -name '*.txt'
CONFIG = -name '$(CONFIG_FILE)'
REMOVE = -exec rm -rf {} +


.SILENT:

all: install

install:
	echo 'Installing dependencies...'
	$(FIND) $(VENV_DIR) $(REMOVE) && \
	$(EXECUTE) $(VENV) && \
	source venv/bin/activate && \
	$(EXECUTE) $(PIP) poetry $(MUTE) && \
	poetry install $(MUTE)
	echo 'Done.'
	echo ''

run: install
	$(EXECUTE) $(MAIN) $(CONFIG_FILE)

debug: install
	echo 'Running in Debug mode'
	echo ''
	$(EXECUTE) $(DEBUG) $(MAIN) $(CONFIG_FILE)

clean:
	echo 'Cleaning caches and temporary files...'
	$(FIND) $(PYCACHE) $(REMOVE)
	$(FIND) $(MYPY_CACHE) $(REMOVE)
	$(FIND) $(TXT) ! $(CONFIG) $(REMOVE)
	$(FIND) $(VENV_DIR) $(REMOVE)
	echo 'Done.'
	echo ''

lint: install
	echo 'Running flake8...'
	$(EXECUTE) $(FLAKE) --exclude venv/
	echo ''
	echo 'Running mypy...'
	$(EXECUTE) $(MYPY) $(MYPY_FLAGS)
	echo 'Done.'
	echo ''

lint-strict: install
	echo 'Running flake8...'
	$(EXECUTE) $(FLAKE) --exclude venv/
	echo ''
	echo 'Running mypy strict...'
	$(EXECUTE) $(MYPY) $(STRICT)
	echo 'Done.'
	echo ''
