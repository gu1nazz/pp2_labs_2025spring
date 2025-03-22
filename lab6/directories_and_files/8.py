import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return
    
    if not os.access(file_path, os.W_OK):
        print("No permission to delete the file.")
        return
    
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")

file_to_delete = input("Enter file path to delete: ")
delete_file(file_to_delete)