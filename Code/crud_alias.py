from shutil import copy
from os import listdir


def create_alias(alias: str, command: str, config: dict):
    """ Create a new alias
    
    Args:
        alias (str): Alias to create
        command (str): Command to create the alias with
        config (dict): Configuration dictionary
    """
    
    alias_txt_file = config["alias_folder"] / f"{alias}.txt"
    new_alias_exe_file = config["alias_folder"] / f"{alias}.exe"
    
    copy(config["alias_exe_launch_file"], new_alias_exe_file)
    
    with open(alias_txt_file, "w") as f:
        f.write(command)

def get_alias(config: dict) -> list[str]:
    """Get a list of all the alias in the alias folder
    
    Args:
        config (dict): Configuration dictionary
    
    Returns:
        list[str]: List of all the alias"""
    alias_files = []
    
    for file in listdir(config["alias_folder"]):
        if file.endswith(".exe"):
            alias_files.append(file.replace(".exe", ""))
    
    return alias_files

def read_alias(alias: str, config: dict) -> str:
    """Read the command of an alias if it exists, otherwise return False
    
    Args:
        alias (str): Alias to read
        config (dict): Configuration dictionary

    Returns:
        str: Command of the alias if it exists, otherwise return False
        False: Alias does not exist"""
    alias_file = config["alias_folder"] / f"{alias}.txt"
    
    try:
        with open(alias_file, "r") as f:
            return f.read()
    except:
        return False

def delete_alias(alias: str, config: dict) -> bool:
    """Delete an alias if it exists, otherwise return False
    
    Args:
        alias (str): Alias to delete
        config (dict): Configuration dictionary
    
    Returns:
        bool: True if the alias was deleted, False if the alias does not exist"""
    
    alias_exe_file = config["alias_folder"] / f"{alias}.exe"
    alias_txt_file = config["alias_folder"] / f"{alias}.txt"
    
    try:
        alias_exe_file.unlink()
        alias_txt_file.unlink()
        return True
    except:
        return False

def update_alias(alias: str, command: str, config: dict) -> bool:
    """Update an alias if it exists, otherwise return False
    
    Args:
        alias (str): Alias to update
        command (str): Command to update the alias with
        config (dict): Configuration dictionary
    
    Returns:
        bool: True if the alias was updated, False if the alias does not exist"""
    
    alias_local = get_alias(config)

    if not alias in alias_local:
        return False
    
    delete_alias(alias, config)
    create_alias(alias, command, config)
    
    return True