MAIN = a_maze_ing.py
CONFIG_FILE = default_config.txt

EXECUTE = python3

FLAKE = -m flake8 .

MYPY = -m mypy .
MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
STRICT = --strict

DEBUG = -m pdb

FIND = find . -type d
PYCACHE = -name '__pycache__'
MYPY_CACHE = -name '.mypy_cache'
REMOVE = -exec rm -rf {} +


.SILENT:

all: install

install:
	echo 'Installing dependencies...'
	poetry install > /dev/null
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
