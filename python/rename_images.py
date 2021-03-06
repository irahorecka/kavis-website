import os
import sys


def parse_filenames(path):
    """Pass in path of directory to change filenames. Do not use this more than once
    if the target directory has already been renamed. This will recursively parse all
    files."""

    def parse_folder(path):
        # Get current directory name
        dir_name = path.split("/")[-1] if path.split("/")[-1] != "" else path.split("/")[-2]
        file_count = 1
        for file in os.listdir(path):
            file = os.path.join(path, file)
            if os.path.isfile(file):
                extension = file.split(".")[-1]
                # Change extensions to be uniform
                if extension in ("JPG", "jpg", "JPEG"):
                    extension = "jpeg"
                try:
                    os.rename(
                        file,
                        os.path.join(path, f"{dir_name}-{f'{file_count:02}.{extension}'}"),
                    )
                    file_count += 1
                except OSError:
                    # Bad file, such as /.DS_Store
                    pass

    directories = [
        os.path.join(path, dir_)
        for dir_ in os.listdir(path)
        if os.path.isdir(os.path.join(path, dir_))
    ]
    if not directories:
        directories = [path]
    list(map(parse_folder, directories))


if __name__ == "__main__":
    arg = sys.argv[1]
    parse_filenames(arg)
