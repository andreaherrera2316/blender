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
