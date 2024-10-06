#!/usr/bin/env python3

import argparse
import os
import sys
from apply_prompt import process_files_with_gpt, process_single_file_with_gpt
from build_template import build_template_from
from folder_struct import folder_struct
from rename_files import rename_files
from replace_in_files import replace_in_files

### COMMANDS ###


def main():
    parser = argparse.ArgumentParser(description="Your Command-Line App")

    subparsers = parser.add_subparsers(dest="subcommand", help="Choose a subcommand")

    ### Subcommand for folder_struct
    folders_parser = subparsers.add_parser(
        "folder_struct",
        description="Create a folder with two files: on file with I prefix for interface and another for it's implementation both with the extension passed in as a param",
        epilog="Usage: blender folder_struct <extension> <folders>...",
    )

    folders_parser.add_argument("extension", help="The file extension")
    folders_parser.add_argument("folders", nargs="+", help="The folder names")

    ### Subcommand for replace_in_files
    replace_parser = subparsers.add_parser(
        "replace_in_files",
        description="Search and replace text in files in a directory",
        epilog="Usage: blender replace_in_files <directory> <find_text> <replace_text> [--file-pattern <file_pattern>]",
    )
    replace_parser.add_argument("directory", help="The directory to search")
    replace_parser.add_argument("find_text", help="The text to find")
    replace_parser.add_argument("replace_text", help="The text to replace")
    replace_parser.add_argument(
        "--file-pattern", default="*", help="File pattern to filter files (default: *)"
    )

    ### Subcommand for rename_files
    rename_parser = subparsers.add_parser(
        "rename_files",
        description="Rename files by replacing a specific word",
        epilog="Usage: blender rename_files <directory> <old_word> <new_word>",
    )
    rename_parser.add_argument("directory", help="The directory to search")
    rename_parser.add_argument("old_word", help="The word to replace")
    rename_parser.add_argument("new_word", help="The word to replace with")

    ### Subcommand for build_template
    build_parser = subparsers.add_parser(
        "build_template",
        description="Build a custom template from a template",
        epilog="Usage: blender build_template <screen_name> [<template_name>] <template_directory> <output_directory>",
    )
    build_parser.add_argument("screen_name", help="The name of the screen")
    build_parser.add_argument(
        "template_name",
        nargs="?",  # This makes template_name optional
        default="Template",  # Default value if not provided
        help="The name of the template (default: 'Template')",
    )
    build_parser.add_argument(
        "template_directory", help="Path to the template directory"
    )
    build_parser.add_argument("output_directory", help="Path to the output directory")

    ### Subcommand for applying GPT prompt
    apply_prompt_parser = subparsers.add_parser(
        "apply_prompt",
        description="Apply a GPT prompt to a file or all files in a directory",
        epilog="Usage: blender apply_prompt <filename_or_directory> <prompt> [--file-pattern <file_pattern>]",
    )
    apply_prompt_parser.add_argument(
        "filename_or_directory", help="File or directory to process"
    )
    apply_prompt_parser.add_argument(
        "prompt", help="The GPT prompt to process each file"
    )
    apply_prompt_parser.add_argument(
        "--file-pattern",
        default="*",
        help="File pattern to filter files in a directory (default: *)",
    )

    args = parser.parse_args()

    if args.subcommand == "replace_in_files":
        replace_in_files(
            args.directory, args.find_text, args.replace_text, args.file_pattern
        )
    elif args.subcommand == "rename_files":
        rename_files(args.directory, args.old_word, args.new_word)
    elif args.subcommand == "build_template":
        # Pass the template_name as an argument
        build_template_from(
            args.screen_name,
            args.template_name,
            args.template_directory,
            args.output_directory,
        )
    elif args.subcommand == "folder_struct":
        folder_struct(args.extension, args.folders)

    elif args.subcommand == "apply_prompt":
        # Process a single file
        if os.path.isfile(args.filename_or_directory):
            process_single_file_with_gpt(args.filename_or_directory, args.prompt)

        # Process all files in the directory matching the file pattern
        elif os.path.isdir(args.filename_or_directory):
            process_files_with_gpt(
                args.filename_or_directory, args.prompt, args.file_pattern
            )
        else:
            print(f"{args.filename_or_directory} is not a valid file or directory.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
