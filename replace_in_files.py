import os
import re
import sys
import fnmatch

def replace_in_files(directory, find_text, replace_text, file_pattern="*"):
    for root, _, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, file_pattern):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                content = re.sub(find_text, replace_text, content)
                with open(file_path, "w") as f:
                    f.write(content)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python replace_in_files.py <find_text> <replace_text> <directory> [file_pattern]")
        sys.exit(1)

    find_text = sys.argv[1]
    replace_text = sys.argv[2]
    directory = sys.argv[3]

    if len(sys.argv) >= 5:
        file_pattern = sys.argv[4]
    else:
        file_pattern = "*"

    replace_in_files(directory, find_text, replace_text, file_pattern)
