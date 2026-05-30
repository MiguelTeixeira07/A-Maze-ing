NAME	= a_maze_ing.py
PYTHON	= python3
CONFIG	= default_config.txt
PIP		= $(PYTHON) -m pip

.SILENT:

all: install

install:
	$(PIP) install --upgrade pip
	$(PIP) install flake8 mypy poetry types-colorama
	$(PYTHON) -m poetry install

dist: install
	poetry build

run: install
	$(PYTHON) $(NAME) $(CONFIG)

debug: install
	$(PYTHON) -m pdb $(NAME) $(CONFIG)

lint: install
	flake8 . --exclude venv
	mypy . --warn-return-any \
	--warn-unused-ignores \
	--ignore-missing-imports \
	--disallow-untyped-defs \
	--check-untyped-defs \
	--exclude 'config.txt' \

lint-strict: install
	flake8 . --exclude venv
	mypy . --strict

clean:
	rm -rf venv/
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.mypy_cache' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

.PHONY: all install run debug lint clean