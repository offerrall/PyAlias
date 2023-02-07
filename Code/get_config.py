from pathlib import Path

def get_config(PROGRAM_FOLDER: Path) -> dict:
    """ Get the configuration of the program
    
    Args:
        PROGRAM_FOLDER (Path): Path of the program folder
    
    Returns:
        dict: Configuration dictionary
    """
    
    config = {}
    config["alias_folder"] = PROGRAM_FOLDER / "Alias/"
    config["code_folder"] = PROGRAM_FOLDER / "Code/"
    config["alias_exe_launch_file"] = config["code_folder"] / "alias_launcher.exe"
    
    if not config["alias_folder"].exists():
        config["alias_folder"].mkdir(parents=True)
    
    if not config["alias_exe_launch_file"].exists():
        raise FileNotFoundError("alias_launcher.exe not found, please reinstall the program")
    
    return config