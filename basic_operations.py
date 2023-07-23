def add_two_numbers(a, b):
    """Add two numbers.

    This function attempts to add two numbers provided as input. If the inputs
    are not valid numbers, it raises a ValueError with a relevant error message.

    Args:
        a: First input value.
        b: Second input value.

    Returns:
        Sum of the two input values.
    """
    error_message = None
    result = None

    # Check if a is a number (either int or float)
    if not isinstance(a, (int, float)):
        error_message = f"First argument {a} is not a valid number."

    # Check if b is a number (either int or float)
    elif not isinstance(b, (int, float)):
        error_message = f"Second argument {b} is not a valid number."

    # If both a and b are valid numbers, perform the addition
    else:
        result = a + b

    # If there's an error message, raise a ValueError with that message
    if error_message:
        raise ValueError(error_message)

    # Return the result
    return result


def safe_divide(a, b):
    result = None
    error_message = None
    
    # Check if inputs are numbers
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        error_message = "Both inputs must be numbers."
    elif b == 0:
        error_message = "Cannot divide by zero."
    else:
        result = a / b

    # If there's an error message, raise it as an exception
    if error_message:
        raise ValueError(error_message)
    
    return result


def modulo(a, b):
    result = None
    try:
        # Convert to int if the input is a string representation of a number
        a = int(a)
        b = int(b)

        # Check for division by zero
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")

        result = a % b
    except ValueError as e:
        # Catch invalid input cases like non-integer strings
        raise ValueError(f"Invalid input: {e}")
    except TypeError:
        # Handle cases where inputs are of invalid types (e.g., lists, dicts)
        raise TypeError("Both inputs must be integers or string representations of integers.")
    
    return result
