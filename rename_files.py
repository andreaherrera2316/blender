import os


def rename_files(directory, old_word, new_word):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if old_word in file:
                new_file = file.replace(old_word, new_word)
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
