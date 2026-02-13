"""Tests for the sample module."""

from reusable_workflows_tester import add_numbers, hello_world, is_even


def test_hello_world() -> None:
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"


def test_add_numbers() -> None:
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(100, 200) == 300


def test_is_even() -> None:
    """Test the is_even function."""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False
