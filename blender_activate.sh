#!/usr/bin/env bash

# Check if the BLENDER_VENV_PATH variable is set
if [ -z "$BLENDER_VENV_PATH" ]; then
    echo "Error: BLENDER_VENV_PATH environment variable is not set.  Please add the path of blenders venv folder in a BLENDER_VIEW_PATH environment variable so the venv can be activated"
    exit 1
fi

# Activate the virtual environment
source "$BLENDER_VENV_PATH/bin/activate"

echo "Virtual environment activated."

