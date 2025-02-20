import os

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)  

def read_file(file_name):
    file_path = f"{file_name}.txt"

    if not os.path.exists(file_path):
        return "File not found"
    
    with open(file_path, "r") as file:
        return file.read()

