from generator import py_generator_split
import pytest


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             ("baby let me iterate ya", "baby"),
                             ("let me iterate ya", "let"),
                             ("me iterate ya", "me")
                         ]
                         )
def test_generator(test_input, expected_output):
    foo = py_generator_split(test_input)
    assert foo.next() == expected_output


