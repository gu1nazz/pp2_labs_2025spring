import os

def check_access(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return
    print("Path exists")
    
    print("Readable" if os.access(path, os.R_OK) else "Not readable")
    print("Writable" if os.access(path, os.W_OK) else "Not writable")
    print("Executable" if os.access(path, os.X_OK) else "Not executable")

path_to_check = "/Users/kassymgulnaz/Documents"  
check_access(path_to_check)
