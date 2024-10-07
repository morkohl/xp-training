import pytest


def convert(arabic):
    return "I"


def test_arabic_1_converts_to_roman_I():
    actual = convert(1)
    assert actual == "I"
