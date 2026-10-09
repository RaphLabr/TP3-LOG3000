from operators import add, subtract, multiply, divide


def test_add():
    """
    Args:
    None

    Returns:
    None
    This test verifies that the addition function ("add") returns the expected result
    """
    assert add(2, 3) == 5
    assert add(2.5, 1.5) == 4.0

def test_subtract():
    """
    Args:
    None

    Returns:
    None
    This test verifies that the subtraction function ("subtract") returns the expected result
    """
    assert subtract(5, 3) == 2
    assert subtract(2.5, 1.5) == 1.0
    assert subtract(3, 5) == -2

def test_multiply():
    """
    Args:
    None

    Returns:
    None
    This test verifies that the multiplication function ("multiply") returns the expected result
    """
    assert multiply(2, 3) == 6
    assert multiply(2.5, 1.5) == 3.75

def test_divide():
    """
    Args:
    None

    Returns:
    None
    This test verifies that the division function ("divide") returns the expected result
    """
    assert divide(6, 3) == 2
    assert divide(7.5, 2.5) == 3.0
    assert divide(7, 2) == 3.5
    assert divide(5, 0) == "Error: Division by zero"