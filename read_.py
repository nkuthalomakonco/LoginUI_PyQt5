
import sys
import pathlib
import os

content = []
path = pathlib.Path(__file__).parent/'user'

#print(f"current_dir: {os.getcwd()}")
#print(f"current_file: {pathlib.Path(__file__)}")

def main():
    print(read_lines_pathlib())

def read_lines(f_name = r'user\user.txt'):
    path = f_name
    if not os.path.exists(path): return []
    with open(path, encoding="utf-8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content
def read_lines_pathlib(f_name = r'user.txt'):
    if not os.path.exists(path/f_name): return []
    with open(path/f_name, encoding="utf-8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content
    
if __name__ == "__main__":
    main()
