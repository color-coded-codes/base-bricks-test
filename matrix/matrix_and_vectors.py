import numpy as np


def list_to_vector(numbers):
    # Ensure input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input should be a list of decimal numbers.")
    
    # Check if the list is empty
    if not numbers:
        raise ValueError("The list is empty.")
    
    # Convert the list to a numpy vector
    try:
        vector = np.array(numbers, dtype=float)
    except ValueError:
        raise ValueError("All elements in the list should be valid decimal numbers.")
    
    # Return the resulting vector
    return vector