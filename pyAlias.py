from typer import Typer
from pathlib import Path
from Code.get_config import get_config
from Code.crud_alias import create_alias, get_alias, read_alias, delete_alias, update_alias
from Code.add_environ import check_path_in_environ, add_new_environ, delete_path_from_environ
from configparser import ConfigParser

PROGRAM_FOLDER = Path(__file__).resolve().parent
app = Typer(add_completion = False)
config = get_config(PROGRAM_FOLDER)


@app.command("new", context_settings = {"ignore_unknown_options": True})
def new(alias: str, command: list[str]):
    '''Create a new alias, EX: pyAlias new ls dir /b'''
    command = " ".join(command)
    create_alias(alias, command, config)
    print(f"Alias created: {alias} -> {command}")

@app.command("list")
def list_alias():
    '''List all aliases'''
    
    alias = get_alias(config)
    
    if not alias:
        print("No alias found")
        return
    
    print(f"Total alias: {len(alias)}")
    for alia in alias:
        alias_data = read_alias(alia, config)
        print(f"- {alia} -> {alias_data}")

@app.command("delete", context_settings = {"ignore_unknown_options": True})
def delete(alias: str):
    '''Delete an alias, EX: pyAlias delete ls'''
    
    if delete_alias(alias, config):
        print(f"Alias deleted: {alias}")
        return
    
    print(f"Alias not found: {alias}")

@app.command("update", context_settings = {"ignore_unknown_options": True})
def update(alias: str, command: list[str]):
    '''Update an alias, EX: pyAlias update ls dir /b'''
    
    command = " ".join(command)
    if update_alias(alias, command, config):
        print(f"Alias updated: {alias} -> {command}")
        return
    
    print(f"Alias not found: {alias}")

@app.command("read")
def read(alias: str):
    '''Read an alias, EX: pyAlias read ls'''
    
    alias_data = read_alias(alias, config)
    
    if not alias_data:
        print(f"Alias not found: {alias}")
        return
    
    print(f"- {alias} -> {alias_data}")

@app.command("paths")
def get_paths():
    '''Get the paths of the program'''
    
    print(f"Program folder: {PROGRAM_FOLDER}")
    print(f"Alias folder: {config['alias_folder']}")

@app.command("install")
def install():
    '''Put the pyAlias folders in the PATH environment variable
    '''
    
    pyalias_alias = "pyalias"
    program_path = str(PROGRAM_FOLDER)
    alias_path = str(config['alias_folder'])

    if check_path_in_environ(program_path):
        print("Program path is already in PATH environment variable")
    else:
        if add_new_environ(program_path):
            print("Added program path to PATH environment variable")

    if check_path_in_environ(alias_path):
        print("Alias path is already in PATH environment variable")
    else:
        if add_new_environ(alias_path):
            print("Added alias path to PATH environment variable")

    if not pyalias_alias in get_alias(config):
        create_alias(pyalias_alias, f"python {PROGRAM_FOLDER}\\pyAlias.py", config)


@app.command("uninstall")
def uninstall():
    '''Remove the pyAlias folders from the PATH environment variable
    '''
    
    program_path = str(PROGRAM_FOLDER)
    alias_path = str(config['alias_folder'])

    if check_path_in_environ(program_path):
        if delete_path_from_environ(program_path):
            print("Removed program path from PATH environment variable")
    else:
        print("Program path is not in PATH environment variable")

    if check_path_in_environ(alias_path):
        if delete_path_from_environ(alias_path):
            print("Removed alias path from PATH environment variable")
    else:
        print("Alias path is not in PATH environment variable")


@app.command("export")
def export():
    '''Export the alias config to a file'''
    
    name = "alias.txt"
    alias = get_alias(config)
    alias_config_file = ConfigParser()
    alias_data = {"alias": {}}

    for alia in alias:
        alias_data["alias"][alia] = read_alias(alia, config)
        
    alias_config_file.read_dict(alias_data)
    
    with open(name, "w") as file:
        alias_config_file.write(file)
    
    print(f"Created file: ./{name} (alias config)")

@app.command("import")
def import_alias(alias_file: str):
    '''Import the alias config from a file'''
    
    alias_file = Path(alias_file)
    if not alias_file.exists():
        print(f"File not found: {alias_file}")
        return
    
    atm_alias = get_alias(config)
    alias_config_file = ConfigParser()
    alias_config_file.read(alias_file)
    alias = alias_config_file["alias"]
    
    for alia in alias:
        if alia in atm_alias:
            update_alias(alia, alias[alia], config)
            continue
        
        create_alias(alia, alias[alia], config)
    
    print(f"Alias imported from {alias_file}")
    

if __name__ == "__main__":
    
    app()
