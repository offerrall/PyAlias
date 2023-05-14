import os
import winreg

def check_path_in_environ(path: str) -> bool:
    """Check if a path is already in the environment variable
    Return:
        bool: True if the path is in the environment variable, False if not
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ) as key:
            current_path = winreg.QueryValueEx(key, "Path")[0]
            return path in current_path.split(";")
    except:
        return False

def add_new_environ(path: str) -> bool:
    """Add a new path to the environment variable
    Return:
        bool: True if the path was added, False if not
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:
            current_path = winreg.QueryValueEx(key, "Path")[0]
            new_path = path + ";" + current_path  # add path at the beginning
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
            os.environ["Path"] = new_path
            return True
    except:
        return False

def delete_path_from_environ(path: str) -> bool:
    """Delete a path from the environment variable
    Return:
        bool: True if the path was deleted, False if not
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:
            current_path = winreg.QueryValueEx(key, "Path")[0]
            path_list = current_path.split(";")
            if path in path_list:
                path_list.remove(path)
                new_path = ";".join(path_list)
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                os.environ["Path"] = new_path
                return True
            else:
                return False
    except:
        return False
