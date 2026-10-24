def add(a,b):
    """
    Args:
    a: float
    b: float

    Returns:
    float
    This function adds two numbers and returns the result
    """
    return a + b

def subtract(a,b):
    """
    Args:
    a: float
    b: float

    Returns:
    float
    This function subtracts two numbers and returns the result
    """
    return a - b

def multiply(a,b):
    """
    Args:
    a: float
    b: float

    Returns:
    float
    This function multiplies two numbers and returns the result
    """
    return a * b

def divide(a,b):
    """
    Args:
    a: float
    b: float

    Returns:
    float
    This function divides two numbers and returns the result
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    else:
        return a / b
