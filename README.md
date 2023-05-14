# PyAlias - A Simple CLI Alias Manager for Windows

PyAlias is a Command Line Interface (CLI) program built with Typer, designed for easy management of aliases in Windows.

## Installation

- Download the repository
- Install dependencies with: `pip install -r requirements.txt`
- Install the program with: `python pyAlias.py install`

## Uninstallation

- Run the program with: `python pyAlias.py uninstall`

## Commands

- `pyalias --help`: Show the program help
- `pyalias new <alias> <command>`: Create a new alias
- `pyalias list`: List all aliases
- `pyalias delete <alias>`: Delete an alias
- `pyalias update <alias> <command>`: Update an alias
- `pyalias read <alias>`: Read an alias
- `pyalias paths`: Get the program paths
- `pyalias install`: Install the program
- `pyalias export`: Export all aliases to a .TXT file
- `pyalias import <file>`: Import aliases from a .TXT file


## Examples
- `pyalias new ls dir /b`: Create a new alias with the name "ls" and the command "dir /b"
- `pyalias update ls dir /b /s`: Update the alias "ls" with the command "dir /b /s"
- `pyalias delete ls`: Delete the alias "ls"



## Functioning

Creating an alias in PyAlias involves two main steps:

1. A .TXT file is created in the `{Program_path}\pyAlias\` folder with the alias name and the assigned command.
2. A copy of `alias_launcher.exe` is made, renamed to the alias, and is responsible for executing the command.

Example:
- If you create an alias named "ls" with the command "dir", running "ls" in the console executes the `ls.exe`, which reads the command from the `ls.txt` file and executes it.


Using a C executable for `alias_launcher` removes Python from the alias execution process, leading to significantly faster alias invocation.
