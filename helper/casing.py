import re
from typing import List


class Casing:
    @staticmethod
    def is_pascal(word: str):
        return bool(re.match(r"^[A-Z][a-zA-Z]*$", word))

    @staticmethod
    def is_camel(word: str):
        return bool(re.match(r"^[a-z][a-zA-Z]*$", word))

    @staticmethod
    def is_snake(word: str):
        return bool(re.match(r"^[a-z]+(_[a-z]+)*$", word))

    @staticmethod
    def camel_case_to_list(word: str):
        parts = [word[0]]
        for char in word[1:]:
            if char.isupper():
                parts.append(char.lower())
            else:
                parts[-1] += char
        return parts

    @staticmethod
    def snake_case_to_list(word: str):
        return word.split("_")

    @staticmethod
    def pascal_case_to_list(word: str):
        parts = [word[0]]
        for char in word[1:]:
            if char.isupper():
                parts.append(char)
            else:
                parts[-1] += char
        return parts

    @staticmethod
    def list_to_camel(word_list: List[str]):
        if not word_list:
            return ""
        return word_list[0].lower() + "".join(
            word.capitalize() for word in word_list[1:]
        )

    @staticmethod
    def list_to_pascal(word_list: List[str]):
        return "".join(word.capitalize() for word in word_list)

    @staticmethod
    def list_to_snake(word_list: List[str]):
        return "_".join(word.lower() for word in word_list)

    @staticmethod
    def to_pascal(word: str):
        word_list = []
        if Casing.is_camel(word):
            word_list = Casing.camel_case_to_list(word)
        elif Casing.is_snake(word):
            word_list = Casing.snake_case_to_list(word)
        return Casing.list_to_pascal(word_list) if word_list else word

    @staticmethod
    def to_camel(word: str):
        word_list = []
        if Casing.is_snake(word):
            word_list = Casing.snake_case_to_list(word)
        elif Casing.is_pascal(word):
            word_list = Casing.pascal_case_to_list(word)
        return Casing.list_to_camel(word_list) if word_list else word

    @staticmethod
    def to_snake(word: str):
        word_list = []
        if Casing.is_camel(word):
            word_list = Casing.camel_case_to_list(word)
        elif Casing.is_pascal(word):
            word_list = Casing.pascal_case_to_list(word)
        return Casing.list_to_snake(word_list) if word_list else word
