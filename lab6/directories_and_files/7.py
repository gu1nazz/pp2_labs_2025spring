import shutil
import os

def copy_file(source):
    if not os.path.exists(source):
        print("File does not exist.")
        return

    dest = source.replace('.', '_copy.', 1)  
    shutil.copy(source, dest)
    print(f"Copied {source} to {dest}")

file_name = input("Enter file name to copy: ")
copy_file(file_name)