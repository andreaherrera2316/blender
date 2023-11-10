import os
import shutil
import sys
from helper.casing import Casing
from rename_files import rename_files
from replace_in_files import replace_in_files


import os
import shutil


def build_template_from(
    screen_name: str, template_name: str, template_directory: str, output_directory: str
):
    # Convert template_name and screen_name to snake and pascal case
    template_snake = Casing.to_snake(template_name)
    template_pascal = Casing.to_pascal(template_name)
    screen_snake = Casing.to_snake(screen_name)
    screen_pascal = Casing.to_pascal(screen_name)

    # Create the output directory
    output_directory = os.path.join(output_directory, screen_snake)

    try:
        # Attempt to copy the contents of the template directory to the output directory
        shutil.copytree(template_directory, output_directory)
    except FileExistsError:
        # If the directory already exists, merge the contents
        for item in os.listdir(template_directory):
            source = os.path.join(template_directory, item)
            destination = os.path.join(output_directory, item)
            if os.path.isdir(source):
                # If it's a directory, recursively merge it
                shutil.copytree(source, destination)
            else:
                # If it's a file, simply copy it over
                shutil.copy2(source, destination)

    # Rename files and replace content in the copied directory
    rename_files(output_directory, template_snake, screen_snake)
    replace_in_files(output_directory, template_pascal, screen_pascal)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python build_template.py <screen_name> <template_directory> <output_directory> <file_pattern>"
        )
        sys.exit(1)

    screen_name = sys.argv[1]
    template_directory = sys.argv[2]
    output_directory = sys.argv[3]
    file_pattern = sys.argv[4]

    build_template_from(screen_name, template_directory, output_directory)
    rename_files(output_directory, "Template", screen_name)
    replace_in_files(output_directory, "template", screen_name.lower())
