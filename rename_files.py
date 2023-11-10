import os


def rename_files(directory, old_word, new_word):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if old_word in file:
                new_file = file.replace(old_word, new_word)
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python rename_word_in_files.py <directory> <old_word> <new_word>")
        sys.exit(1)

    directory = sys.argv[1]
    old_word = sys.argv[2]
    new_word = sys.argv[3]

    rename_files(directory, old_word, new_word)
