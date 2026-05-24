MAIN = a_maze_ing.py
CONFIG_FILE = default_config.txt

EXECUTE = python3

FLAKE = -m flake8 .

MYPY = -m mypy .
MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
STRICT = --strict

DEBUG = -m pdb

FIND = find .
FOLDER = -type d
FILE = -type f
PYCACHE = -name '__pycache__'
REMOVE = rm -rf


all: install

install:
	poetry install

run: install
	$(EXECUTE) $(MAIN) $(CONFIG_FILE)

debug:
	$(EXECUTE) $(DEBUG) $(MAIN) $(CONFIG_FILE)

clean:
	$(FIND) $(FOLDER) $(PYCACHE) -exec $(REMOVE) {}

lint:
	$(EXECUTE) $(FLAKE)
	$(EXECUTE) $(MYPY) $(MYPY_FLAGS)

lint-strict:
	$(EXECUTE) $(FLAKE)
	$(EXECUTE) $(MYPY) $(STRICT)
