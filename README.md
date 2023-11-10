# Blender

Blender File Manipulation and Template Customization Script

## Overview

Blender is a small scripting project designed to perform three main functions on files within a directory. These functions include:

1. **rename_files:** Rename files by replacing a specific word.
2. **replace_in_files:** Search and replace text in files within a directory.
3. **build_template:** Create a custom copy from a template.

## Usage

### 1. rename_files

Rename files by replacing a specific word in their names.

```bash
blender rename_files <directory> <old_word> <new_word>
```

**Arguments:**

- `<directory>`: The directory containing the files to be renamed.
- `<old_word>`: The word to be replaced in file names.
- `<new_word>`: The word to replace `<old_word>` in file names.

**Example:**

```bash
blender rename_files /path/to/files old_name new_name
```

### 2. replace_in_files

Search and replace text in files within a directory.

```bash
blender replace_in_files <directory> <find_text> <replace_text> [--file-pattern <file_pattern>]
```

**Arguments:**

- `<directory>`: The directory containing the files to be processed.
- `<find_text>`: The text to be replaced.
- `<replace_text>`: The text to replace `<find_text>` with.
- `[--file-pattern]` (Optional): File pattern to filter files (default: `*`).

**Example:**

```bash
blender replace_in_files /path/to/files old_text new_text --file-pattern *.txt
```

Certainly! The `build_template` command is designed to facilitate the creation of a customized template from an existing template. Let's break down how it works:

## Notes

- For `rename_files` and `replace_in_files`, the script processes all files in the specified directory.
- Use the optional `--file-pattern` argument with `replace_in_files` to filter files based on a specific pattern.

### 3. build_template

Build a custom template from an existing template.

### DEMO VIDEO:

https://drive.google.com/file/d/1YUlw4QCUbJ4hSEV6HHc29VorRcr0uRY7/view?usp=drive_link

```bash
blender build_template <screen_name> [<template_name>] <template_directory> <output_directory>
```

**Arguments:**

- `<screen_name>`: The name of the screen or module you are creating.
- `[<template_name>]` (Optional): The name of the existing template (default: 'Template').
- `<template_directory>`: Path to the directory containing the existing template files.
- `<output_directory>`: Path to the directory where the customized template will be created.

#### How It Works:

1. **Specify Screen Name:**

   - `<screen_name>` is the name of the screen or module you are creating. It's the identifier for the new template.

2. **Specify Template Name (Optional):**

   - `[<template_name>]` is an optional argument to specify the name of the existing template. If not provided, it defaults to 'Template'. This is the base template that you want to customize.

3. **Specify Template Directory:**

   - `<template_directory>` is the path to the directory containing the existing template files. This directory should have files related to the template, such as `template.dart` and `template_view.dart`.

4. **Specify Output Directory:**
   - `<output_directory>` is the path to the directory where the customized template will be created. This is where the modified template files will be stored.

#### Example:

Suppose you have an existing template in the directory `/path/to/template`. In this directory, there is a file named `template.dart` containing the class `Template{}`, and another file named `template_view.dart` with the class `TemplateView{}`.

When you run the `build_template` command as shown in the example:

```bash
blender build_template my_screen CustomTemplate /path/to/template /path/to/output
```

The script will:

- Identify all occurrences of the word 'template' in file names and rename them in snake_case to the specified template name, which is 'custom_template' in this case.

  - `template.dart` becomes `custom_template.dart`
  - `template_view.dart` becomes `custom_template_view.dart`

- Recognize PascalCase occurrences of the word 'template' within files and replace them with the specified template name.
  - `class Template {}` becomes `class CustomTemplate {}`
  - `class TemplateView {}` becomes `class CustomTemplateView {}`

The result is a customized template in the specified output directory ready for use in your project.

# INSTALLATION GUIDE

## MACOS SET UP

### 1. Download the Repository

- First, clone or download this repository to your home directory:

```bash
cd ~
git clone https://github.com/andreaherrera2316/blender
```

### 2. Set Up the Soft Link

- To make it easier to execute the `blender` command, you can set up a soft link in a directory that's included in your system's PATH. In this example, we'll set it up in the `/usr/local/bin/` directory:

```bash
sudo ln -s ~/blender/blender.py /usr/local/bin/blender
```

- This command creates a soft link named `blender` that points to the `blender.py` script within the cloned repository.

### 3. Provide Executable Permissions

Make sure that the soft link is executable. You can do this with the following command:

```bash
sudo chmod +x /usr/local/bin/blender
```

This command grants the necessary permissions for the `blender` command to be run

Congratulations! You're all set in Mac! You can now use the `blender` command for everyday tasks, and duplicate templates in a custom way

## WINDOWS SETUP

### 1. Navigate to Home Directory

- Open a Command Prompt and navigate to your home directory. Replace `<username>` with your Windows username:

```bash
cd C:\Users\<username>
```

### 2. Download the Repository

- Clone or download this repository to your home directory:

```bash
git clone https://github.com/andreaherrera2316/blender
```

### 3. Navigate to the Blender Directory

- Change your current directory to the newly cloned "blender" directory:

```bash
cd blender
```

### 4. Create a Batch Script for Easy Access

- Create a batch script named `blender.bat` in the same directory as `blender.py`. Open a text editor and add the following content:

```batch
@echo off
python blender.py %*
```

- Save the file in the "blender" directory.

### 5. Add the Blender Directory to PATH

- To run `blender` from any location, add the full path of the "blender" directory to the system's PATH environment variable.

  - Right-click on "This PC" or "Computer" on your desktop or in File Explorer.
  - Select "Properties."
  - Click on "Advanced system settings" on the left.
  - Click on the "Environment Variables" button.
  - In the "System variables" section, select "Path" and click "Edit."
  - Click "New" and add the full path to the "blender" directory (e.g., `C:\Users\<username>\blender`).

### 6. Run Blender from Any Directory

- Open a new Command Prompt and run `blender <command>` from any directory:

```bash
blender <command>
```

Now, you can use the `blender` command from any location on your system without specifying the full path. The batch script (`blender.bat`) ensures that the Python interpreter is used to execute the `blender.py` script.
