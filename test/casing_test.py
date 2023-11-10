from helper.casing import Casing
import pytest


def test_is_pascal():
    assert Casing.is_pascal("PascalCase") == True
    assert Casing.is_pascal("camelCase") == False


def test_is_camel():
    assert Casing.is_camel("camelCase") == True
    assert Casing.is_camel("snake_case") == False


def test_is_snake():
    assert Casing.is_snake("snake_case") == True
    assert Casing.is_snake("PascalCase") == False


def test_camel_case_to_list():
    assert Casing.camel_case_to_list("camelCaseExample") == ["camel", "Case", "Example"]


def test_snake_case_to_list():
    assert Casing.snake_case_to_list("snake_case_example") == [
        "snake",
        "case",
        "example",
    ]


def test_pascal_case_to_list():
    assert Casing.pascal_case_to_list("PascalCaseExample") == [
        "Pascal",
        "Case",
        "Example",
    ]


def test_list_to_camel():
    assert (
        Casing.list_to_camel(["this", "is", "a", "sample", "list"])
        == "thisIsASampleList"
    )


def test_list_to_pascal():
    assert (
        Casing.list_to_pascal(["this", "is", "a", "sample", "list"])
        == "ThisIsASampleList"
    )


def test_list_to_snake():
    assert (
        Casing.list_to_snake(["this", "is", "a", "sample", "list"])
        == "this_is_a_sample_list"
    )


def test_to_pascal():
    assert Casing.to_pascal("camelCaseExample") == "CamelCaseExample"
    assert Casing.to_pascal("snake_case_example") == "SnakeCaseExample"


def test_to_camel():
    assert Casing.to_camel("snake_case_example") == "snakeCaseExample"
    assert Casing.to_camel("PascalCaseExample") == "pascalCaseExample"


def test_to_snake():
    assert Casing.to_snake("camelCaseExample") == "camel_case_example"
    assert Casing.to_snake("PascalCaseExample") == "pascal_case_example"
