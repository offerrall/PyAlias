import os
import winreg

def add_new_environ(path: str) -> bool:
    """Add a new path to the environment variable
    Return:
        bool: True if the path was added, False if not
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS) as key:
            current_path = winreg.QueryValueEx(key, "Path")[0]
            if path not in current_path.split(";"):
                new_path = current_path + ";" + path
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        
        os.environ["Path"] = new_path
        return True
    except:
        return False
