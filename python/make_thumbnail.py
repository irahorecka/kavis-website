import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAR_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

def recurse_resize(path):
    for item in os.listdir(path):
        if item == ".DS_Store":
            continue
        item = os.path.join(path, item)
        if os.path.isdir(item):
            recurse_resize(item)
        else:
            subprocess.Popen(f'make resize-800-600 IN={item}', shell=True)
            # os.rename(item, item.replace('.JPG', '.jpeg'))

def main():
    os.chdir(PAR_DIR)
    thumbnail_dir = os.path.join(PAR_DIR, 'assets', 'images', 'photos', 'thumbnail')
    recurse_resize(thumbnail_dir)

if __name__ == "__main__":
    main()
