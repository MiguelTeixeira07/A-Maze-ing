*This project has been created as part of the 42 curriculum by migteixe, vmesini-*

# A-Maze-ing

## Description

A-Maze-ing is a Python project that generates and solves mazes directly in the terminal.

The goal of the project is to create a configurable maze generator that can:
- Generate valid mazes using a chosen algorithm.
- Display the maze in a clear and colorful format.
- Mark the entry and exit points.
- Display the solution path.
- Load settings from a configuration file.
- Opitionally:
    - Regenerates a new maze
    - Show/Hide path from entry to exit
    - Rotate maze colors


The project was designed with modularity in mind, allowing the maze generation logic, rendering, and configuration handling to be reused independently.

---

## Features

- Procedural maze generation.
- Maze solving.
- Terminal rendering with ANSI colors.
- Customizable colors through configuration.
- Optional logo and visual enhancements.
- Installable Python package.
- Dependency management with Poetry.

---

## Instructions

### Requirements

- Python 3.x
- Poetry
- Colorama

### Installation

```bash
git clone https://github.com/MiguelTeixeira07/A-Maze-ing.git
cd A_Maze_ing
```

### Execution

- Run the code program:
```bash
python3 a_maze_ing.py <configuration_file.txt>
```
- Select numbers 1 to 3 to interact with the maze and 4 to quit interaction

### Resources

- Ansi modification with Colorama module: https://youtu.be/u51Zjlnui4Y?si=EuRzDpFR6vMIDwmI
- Learning how to use git on a group porject: https://youtu.be/jhtbhSpV5YA?si=JZ17voALXAW4ffzB

### AI Usage

Artificial intelligence tools were used as a supporting resource throughout the development of this project. Their role was limited to guidance, clarification, and review; all design decisions, implementation, debugging, and final integration were carried out manually.

AI was used for the following tasks:

- Git and GitHub workflow support
- Understanding how branches, merges, rebases, pull requests, and detached HEAD states work.
- Resolving merge conflicts.
- Project structure and packaging
- Documentation
- Writing and refining docstrings.
- Structuring this README.md according to 42 project requirements.
- Code organization and refactoring
- Discussing ways to improve class design and separate responsibilities, particularly in the display and maze modules.
- Clarifications about imports, ANSI color codes and standard Python behavior.

AI was not used to generate the project architecture or final implementation automatically. All code included in the final submission was written, reviewed, tested, and adapted manually by the authors. AI-generated suggestions were treated as reference material and were only incorporated after being fully understood and validated.


## Config File Structure

- WIDTH
- HEIGHT
- ENTRY
- EXIT
- OUTPUT_FILE (file that has hexdecimal maze, entry/exit points and path directions)
- PERFECT (True or False)

## Chosen algorithm

## Code Reusability

- mazegen module is reusable, by adding an \__init__.py inside the directory and adding mazegen in .toml file with poetry add mazegen

## Project Management

### Team Roles

- vmesini-: Responsible for the display part (ANSI, walls and path), user interation menu and Makefile
- migteixe: Responsible for maze generation/solving algorithms and anything else related with the maze backend, such as generating the output file.
- Both parts were tested by both members of the group and both parties helped solve each other's errors.

### Anticipated planning and expectations

### Possible Improvements

### Specific Tools Used