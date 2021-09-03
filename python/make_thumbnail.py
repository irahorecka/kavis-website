import os
import subprocess
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAR_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


def recurse_resize(path):
    """Recursively resize images in target directory."""
    for item in os.listdir(path):
        if item == ".DS_Store":
            continue
        item = os.path.join(path, item)
        if os.path.isdir(item):
            recurse_resize(item)
        else:
            subprocess.Popen(f"make resize-1200-900 IN={item}", shell=True)


if __name__ == "__main__":
    path = sys.argv[1]
    recurse_resize(path)
