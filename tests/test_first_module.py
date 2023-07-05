import pytest

from python_caching.first_module import foo, is_foo


def test_foo():
    assert foo() == "foo"


@pytest.mark.parametrize("input,expected", [("foo", True), ("bar", False)])
def test_is_foo(input, expected):
    assert is_foo(input) == expected
