def add_two_numbers(a, b):
    """
    ![Alt text](https://images.unsplash.com/photo-1508009603885-50cf7c579365?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1950&q=80)
    # Heading 1
    ## Heading 2
    ### Heading 3
    #### Heading 4
    ##### Heading 5
    ###### Heading 6
    
    Lorem **ipsum dolor** sit amet, [Google](https://www.google.com) consectetur adipiscing elit. Curabitur rhoncus, justo eget volutpat semper, erat sapien mollis elit, eget congue est augue et metus. Proin sit amet libero id eros vestibulum consequat. Vivamus posuere, elit vitae interdum sollicitudin, risus justo egestas velit, vitae dapibus odio orci vitae nunc.
    
    **Fusce sed enim volutpat**, Lorem *ipsum dolor sit amet*, consectetur adipiscing elit. Curabitur rhoncus, justo eget volutpat semper, erat sapien mollis elit, eget congue est augue et metus. Proin sit amet libero id eros vestibulum consequat. Vivamus posuere, elit vitae interdum sollicitudin, risus justo egestas velit, vitae dapibus odio orci vitae nunc. Fusce sed enim volutpat.

    Fusce sed enim volutpat:
    - Item 1
    - Item 2

    ---
    Fusce sed enim volutpat:
    1. First item
    2. Second item

    > This is a blockquote

    `requirements==1.2`

    And a code blpck here:

    ```
    from django.conf import settings

    for x in y:
        print(x)
    
    
    ```
    ---

    For each thing there is a ~~strikethrough~~ to show!

    | Header 1 | Header 2 |
    |----------|----------|
    | Cell 1   | Cell 2   |
    | Cell 3   | Cell 4   |

    - [x] Task 1 (completed)
    - [ ] Task 2 (not completed)

    is this emoji working?? :smile:

    Term 1
    : Definition 1

    Term 2
    : Definition 2

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
