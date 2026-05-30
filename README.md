*This project has been created as part of the 42 curriculum by migteixe, vmesini-*

# A-Maze-ing

## Description

A-Maze-ing is a Python project that is both a maze generator and solver program.

The goal of the project is to create a configurable maze generator that can:
- Generate valid mazes using a chosen algorithm.
- Display the maze in a clear and colorful format.
- Mark the entry and exit points.
- Display the solution path.
- Load settings from a configuration file.
- Give the user the choice to:
    - Regenerates a new maze
    - Show/Hide path from entry to exit
    - Rotate maze colors


The project was designed with modularity in mind, allowing the maze generation logic, rendering, and configuration handling to be reused independently.

---

## Features

- Maze generation.
- Maze solving.
- Maze terminal rendering with ANSI colors.
- Randomize colors through user interation menu.
- Installable Python package.
- Dependency management with Poetry.

---

## Instructions

### Requirements

- Python 3.x
- Poetry
- Colorama

### Installation
First, clone the repository:
```bash
git clone <repository_link>
cd A_Maze_ing
```
When the repository is cloned, install all of the required project dependencies (it is recomended that for this step you use a virtual environment, also note that if the virtual environment you use is inside the project folder, there will be flake8 errors related to it):
```bash
make
```
```bash
make install
```
```bash
poetry install
```
If there are any errors related to the installation of poetry through pip, try installing it manually with the following command:
```bash
pip install poetry
```
If errors prevail, try updating pip:
```bash
pip install update
pip install --upgrade pip
```

### Execution

- Run the code program:
```bash
python3 a_maze_ing.py <configuration_file.txt>
```
Anternatively, you can run:
```bash
make run
```
and use the default config file provided

## Configuration
*The configuration of the maze will be made through the configuration file. This file will treat the flags by name and not order*

```
FLAG=<value>
```

- Available flags:
    - WIDTH <x> (min=9, max=40)
    - HEIGHT <x> (min=7, max=40)
    - ENTRY <x,y>
    - EXIT <x,y>
    - OUTPUT_FILE <file.txt>
    - PERFECT <True/False>
*Note that every flag listed needs to be on the configuration file*

## Chosen algorithms
*This program uses a total of 2 perfect maze generation algorithms and an additional maze braiding algorithm that can be based on either one of the perfect maze generation algorithms.*

- Depth-First Search
- Hunt and Kill

### Depth-First Search
The depth-first search algorithm starts the generation on the entry of the maze.
While the maze is not fully generated, the algorithm will pick a random direction and move there if it has not been visited yet.
When the algorithm gets to a dead-end, it traces back the path it made there until it finds a cell that has neighbours which have not been visited yet.
If it backtracks all the way back to the entry of the maze, then it means all the cells have been visited, therefore the maze has been fully generated, with all cells accessible (for the sole exception of the 42 pattern cells).

### Hunt and Kill
The hunt and kill algorithm starts the generation on the entry of the maze.
While the maze is not fully generated, the algorithm will pick a random direction and move there if it has not been visited yet.
When the algorithm gets to a dead-end, it looks from top to bottom and left to right of the maze until it finds a visited cell that has neighbours which have not been visited yet.
If it gets to the bottom-right corner of the maze while looking for a cell to proceed maze generation and doesn't find any, then it means all the cells have been visited, therefore the maze has been fully generated, with all cells accessible (for the sole exception of the 42 pattern cells).

## Code Reusability

The mazegen module is reusable, by adding an \_\_init\_\_.py inside the directory and adding mazegen in .toml file with poetry add mazegen

## Project Management

### Team Roles

- vmesini-: Responsible for the display part (ANSI, walls and path) and the user interation menu.
- migteixe: Responsible for maze generation/solving algorithms and anything else related with the maze backend, such as generating the output file and the makefile.
- Both parts were tested by both members of the group and both parties helped solve each other's errors.

### Anticipated planning and expectations
Originally, the time estimate to do this project was about 2 weeks. However, these 2 weeks later turned to approximately 4 due to some hurdles like project version management and comunication between the 2 developers.
The development process itself went quite smoothly, but the main setback was all the documentation and formalities required by the 42 standards, such as mypy, flake8 and code documentation standards like the requirement to write docstrings in every function.
Aside from this, the project difficulty and complexity met the initial expectations and everything went according to plan.

### Possible Improvements
The project meets all the functional and stylistic requirements, and we focused on high code quality and clear project management. One area that could be explored further is experimenting with alternative design patterns.
Automated tests could also have been added to provide help in debugging during the project's development process.

### Specific Tools Used
#### Git
Git was used for project and version management purposes, where each party had a different branch and experimental versions and tests were merged into a "dev" branch. When a version was stable and good enough for setting a baseline of what the project was looking like, dev was merged into main.

### Resources

- Ansi modification with Colorama module: https://youtu.be/u51Zjlnui4Y?si=EuRzDpFR6vMIDwmI
- Learning how to use git on a group porject: https://youtu.be/jhtbhSpV5YA?si=JZ17voALXAW4ffzB
- Basic maze related logic and algorithms: http://youtube.com/watch?v=uctN47p_KVk&t=370s

### AI Usage

Artificial intelligence tools were used as a supporting resource throughout the development of this project. Their role was limited to guidance, clarification, and review; all design decisions, implementation, debugging, and final integration were carried out manually.

AI was used for the following tasks:

- Git and GitHub workflow support
- Project structure and packaging.
- Code organization and refactoring.
- Clarifications about imports, ANSI color codes and standard Python behavior.
- Documentation and README.md file development.

AI was not used to generate the project architecture or final implementation automatically. All code included in the final submission was either written, reviewed, tested, or adapted manually by the authors. AI-generated code snippets were treated as reference material and were only incorporated after being validated and fully understood.