def add_two_numbers(a, b, options):
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


def modulo(a=1, b=3):
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


def str2int(text):
    try:
        integer_number = int(text)
    except ValueError:
        integer_number = 0
    
    return integer_number


def generate_random_numbers():
    import random
    random_array = [random.randint(1, 100) for _ in range(100)]
    return random_array


def compute_mean(numbers):
    if len(numbers) == 0:
        result = 0
    else:
        result = sum(numbers) / len(numbers)
    return result

def number_of_characters(text):
    result = len(text)
    return result


def generate_fake_dicts(num_dicts=10):
    import random
    import string
    def random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def random_int(min_val=1, max_val=100):
        return random.randint(min_val, max_val)
    
    keys = ['name', 'age', 'address']
    fake_dicts = []
    
    for _ in range(num_dicts):
        fake_dict = {}
        for key in keys:
            random_type = random.choice(['str', 'int'])
            if random_type == 'str':
                fake_dict[key] = random_string()
            else:
                fake_dict[key] = random_int()
        fake_dicts.append(fake_dict)
    
    return fake_dicts


def as_is(number):
    return number