import os
from typing import List


def folder_struct(extension: str, folders: List[str]):
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, f"{folder}.{extension}"), "w") as f:
            f.write("")
        with open(os.path.join(folder, f"I{folder}.{extension}"), "w") as f:
            f.write("")
