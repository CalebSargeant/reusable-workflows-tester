"""Sample module for testing the reusable-workflows CI/CD pipeline."""


def hello_world() -> str:
    """Return a hello world greeting.

    Returns:
        str: A greeting message
    """
    return "Hello, World!"


def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        int: Sum of a and b
    """
    return a + b


def is_even(n: int) -> bool:
    """Check if a number is even.

    Args:
        n: Number to check

    Returns:
        bool: True if n is even, False otherwise
    """
    return n % 2 == 0
