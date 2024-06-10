import os
import shutil
import sys
from helper.casing import Casing
from rename_files import rename_files
from replace_in_files import replace_in_files


def build_template_from(
    screen_name: str, template_name: str, template_directory: str, output_directory: str
):
    # Convert template_name and screen_name to snake and pascal case
    template_snake = Casing.to_snake(template_name)
    template_pascal = Casing.to_pascal(template_name)
    screen_snake = Casing.to_snake(screen_name)
    screen_pascal = Casing.to_pascal(screen_name)

    # Create the output directory
    # output_directory = os.path.join(output_directory, screen_snake)

    try:
        # Attempt to copy the contents of the template directory to the output directory
        shutil.copytree(template_directory, screen_snake)  # walk the directory insetead
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
