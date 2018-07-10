#!/usr/bin/env python

"""
test code for capitalize module

can be run with py.test
"""

import os
from pathlib import Path

import pytest

import capital_mod

# fixture that creates and removes a file with special words in it
@pytest.fixture(scope='module')
def special_words_path():
    """
    fixture to generate a special words file to test reading

    Note: probably better to use a tempfile.NamedTemporaryFile,
          but this is a bit more straightforward
    """
    # A couple words for the file
    words = ["in", "As", "the"]
    temp_path = Path("special_words_file")
    with open(temp_path, 'w') as outfile:
        for word in words:
            outfile.write(word + "\n")
        # test comments, too:
        outfile.write("# random stuff")
        outfile.write("  in  # comment after a word\n")
    # the file wil be created and filled, then the path passed on
    yield temp_path
    # at "teardown", the file will be removed
    os.remove(temp_path)


# fixture that creates and removes a file with some test lines in it.
@pytest.fixture(scope='module')
def test_file_path():
    """
    Fixture to generate a file with some sample data in it
    """
    # A couple words for the file
    temp_path = Path("input_test_file.txt")
    with open(temp_path, 'w') as outfile:
        outfile.write("""This is a really simple Text file.
It is here so that I can test the capitalize script.

And that's only there to try out packaging.

So there.
""")
    # the file wil be created and filled, then the path passed on
    yield temp_path
    # at "teardown", the file will be removed
    os.remove(temp_path)


def test_load_special_words(special_words_path):
    """
    test that the special words are properly loaded
    """
    words = capital_mod.load_special_words(special_words_path)
    assert "in" in words
    assert "the" in words
    assert "as" in words


def test_capitalize_line():
    special = {'is', 'a', 'to'}
    line =     "this is a Line to capitalize"
    expected = "This is a Line to Capitalize"

    result = capital_mod.capitalize_line(line, special_words=special)
    assert  result == expected

def test_capitalize(test_file_path):
    """ test an actual file """
    p = test_file_path

    new_file_path = (p.parent / (p.stem + "_cap")).with_suffix(p.suffix)

    capital_mod.capitalize(p, new_file_path)

    contents = open(new_file_path).read()
    expected = """This is a Really Simple Text File.
It is Here So That I Can Test the Capitalize Script.

And That's Only There to Try Out Packaging.

So There."""
    assert contents.strip() == expected 



