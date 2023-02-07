# PyAlias - A Simple CLI Alias Manager for Windows

PyAlias is a Command Line Interface (CLI) program built with Typer, designed for easy management of aliases in Windows.

## Installation

- Download the repository
- Install dependencies with: `pip install -r requirements.txt`
- Install the program with: `python pyAlias.py install`

## Uninstallation

- Delete the environment variables, {Program_path} and {Program_path}\pyAlias\

## Commands

- `pyalias help`: Show the program help
- `pyalias new <alias> <command>`: Create a new alias
- `pyalias list`: List all aliases
- `pyalias delete <alias>`: Delete an alias
- `pyalias update <alias> <command>`: Update an alias
- `pyalias read <alias>`: Read an alias
- `pyalias paths`: Get the program paths
- `pyalias install`: Install the program

## Functioning

When creating an alias, a .TXT file is created in the folder {Program_path}\pyAlias\ with the alias name and the assigned command.
A copy of alias_launcher.exe is also created in the folder {Program_path}\pyAlias\ and is assigned the alias name.
alias_launcher.exe is a C program that is responsible for executing a command in the console.
alias_launcher.exe reads its name and uses it to read the .TXT file with the same name and execute the command it contains.
alias_launcher.exe will also take its arguments and pass them to the command it contains.

Example:
- You create an alias with the name "ls" and the command "dir"
- A .TXT file is created in the folder {Program_path}\pyAlias\ with the name "ls" and the content "dir"
- A copy of alias_launcher.exe is created in the folder {Program_path}\pyAlias\ and is assigned the name "ls"
- When you run the "ls" command in the console, the file {Program_path}\pyAlias\ls.exe is executed
- ls.exe reads its name and uses it to read the .TXT file with the same name and execute the command it contains.
- ls.exe will also take its arguments and pass them to the command it contains.

alias_launcher is a .exe and .c file, so it can be changed to suit your needs.
