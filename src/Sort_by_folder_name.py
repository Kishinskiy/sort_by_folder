import os
import shutil
import zipfile
from tqdm import tqdm

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="folder with zip files", type=str)
args = parser.parse_args()

def sort_files():
    for root, _, files in os.walk(os.path.abspath(args.folder), topdown=False):
        files.sort()
        for name in tqdm(files):
            folder_name = os.path.join(name[0])
            try:
                if not os.path.exists(root + "/" + folder_name):
                    os.mkdir(root + "/" + folder_name)
                shutil.move(root + "/" + name, root + "/" + folder_name)
            except Exception as e:
                print(e, name)


def sort_dirs(path, arg):
    arg.sort()
    for name in tqdm(arg):
        folder = name.split("-")
        folder_name = folder[1].strip()
        if not os.path.exists(path + folder_name):
            os.mkdir(path + folder_name)
        shutil.move(path + "/" + name, path + "/" + folder_name + "/" + folder[2].strip())


def unzip_files():
    for root, dirs, files in os.walk(os.path.abspath(args.folder), topdown=False):
        for name in tqdm(files):
                try:
                    with zipfile.ZipFile(root + "/" + name, 'r') as zip_ref:
                        zip_ref.extractall(root)
                    os.remove(root + "/" + name)
                except Exception as e:
                    print(e)


if __name__ == '__main__':
   sort_files()
   unzip_files()
