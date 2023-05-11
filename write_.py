
import sys
import pathlib
import os


path = pathlib.Path(__file__).parent/'user'

def main():
    print(write_pathlib("[Done] exited with code=0 in 0.297 seconds"))
def write_(content="",f_name = r'xxx.txt'):
    path = pathlib.Path(__file__).parent/'user'/f_name
    with open(f_name, "a") as f:
        f.write(content)
    return 1
def write_pathlib(content="",f_name = r'xxx.txt'):
    path = pathlib.Path(__file__).parent/'user'/f_name
    path.write_text(content)
    print(pathlib.Path(path).parent)
    if path.is_file(): return True
    return False
if __name__ == "__main__":
    main()