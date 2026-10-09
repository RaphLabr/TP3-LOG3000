from app import calculate
import pytest

def test_calculate_addition():
    """
    Args:
    None

    Returns:
    None
    This test verifies that calculate returns the correct result
    for a valid addition expression
    """
    assert calculate("5+3") == 8.0


def test_calculate_decimal_numbers():
    """
    Args:
    None

    Returns:
    None
    This test verifies that calculate supports decimal numbers as operands
    """
    assert calculate("2.5+1.5") == 4.0


def test_calculate_empty_expression():
    """
    Args:
    None

    Returns:
    None
    This test verifies that an empty expression raises ValueError
    """
    with pytest.raises(ValueError):
        calculate("")    


def test_calculate_missing_operator():
    """
    Args:
    None

    Returns:
    None
    This test verifies that an expression without an operator is rejected 
    and raises a ValueError
    """
    with pytest.raises(ValueError):
        calculate("53")


def test_calculate_missing_operand():
    """
    Args:
    None

    Returns:
    None
    This test verifies that an expression with a missing operand is rejected 
    and raises a ValueError
    """
    with pytest.raises(ValueError):
        calculate("5+")


def test_calculate_multiple_operators():
    """
    Args:
    None

    Returns:
    None
    This test verifies that expressions with more than one operator are rejected
    and raise a ValueError
    """
    with pytest.raises(ValueError):
        calculate("5+3-2")
        calculate("5+*2")


def test_calculate_non_numeric_operand():
    """
    Args:
    None

    Returns:
    None
    This test verifies that non-numeric operands are rejected and raise a ValueError
    """
    with pytest.raises(ValueError):
        calculate("abc+3")