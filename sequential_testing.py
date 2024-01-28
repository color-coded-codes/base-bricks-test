def read_text_file(file_path):
    import os

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    # Check if the path is a directory
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"'{file_path}' is a directory, not a file.")

    # Try to open and read the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Return the content as text
    return file_content


def generate_random_text(n, options):
    import random
    import string
    # Split the reference text into words
    generate_words = options['is_words']
    reference_text = options['reference_text']

    if generate_words:
        words = reference_text.split()

        # Ensure n is non-negative
        n = max(n, 0)

        # Generate the new text by randomly selecting words
        generated_words = [random.choice(words) for _ in range(n)]

        # Combine the generated words into a text
        generated_text = ' '.join(generated_words)
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + ' '
        generated_text = ''.join(random.choice(characters) for _ in range(n))

    return generated_text


def generate_random_integer(options):
    import random

    min_value = options['min_value']
    max_value = options['max_value']
    random_integer = random.randint(min_value, max_value)
    
    return random_integer


def create_file_with_content(text_content, file_path, file_name):
    import os
    
    # Ensure the directory structure exists
    os.makedirs(file_path, exist_ok=True)
    
    # Combine the file path and name
    file_location = os.path.join(file_path, file_name)
    
    # Write the text content to the file
    with open(file_location, 'w') as file:
        file.write(text_content)
    
    return file_location


def list_files_in_folder(folder_path):
    import os
    
    file_list = []
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            # Get the file size in kilobytes
            file_size_kb = os.path.getsize(file_path) / 1024.0
            
            # Create a dictionary object for each file
            file_info = {
                "file_name": file_name,
                "file_size_kb": file_size_kb
            }
            
            file_list.append(file_info)
    
    return file_list


def get_values_from_list_of_dicts(dict_list, key):
    values_list = [d[key] for d in dict_list if key in d]
    return values_list


def count_characters(text):
    char_count = len(text)
    return char_count


def count_words(text):
    import re
    
    words = re.findall(r'\w+', text)
    word_count = len(words)
    
    return word_count


def create_folder_if_not_exists(folder_path):
    import os
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path



def move_file(source_path, destination_folder):
    import shutil
    
    shutil.move(source_path, destination_folder)



def update_file_name(old_file_path, new_file_name):
    import os
    
    # Extract the directory path and the current file name
    directory_path, current_file_name = os.path.split(old_file_path)
    
    # Create the new file path with the updated name
    new_file_path = os.path.join(directory_path, new_file_name)
    
    # Rename the file with the new name
    os.rename(old_file_path, new_file_path)
    
    return new_file_path


def delete_file(file_path):
    import os
    
    os.remove(file_path)


def concatenate_strings_with_separator(string1, string2, options):
    separator=options['separator']
    result_string = string1 + separator + string2
    return result_string


def parse_integer_to_text(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    text_representation = str(number)
    
    return text_representation


def generate_random_integers(n):
    from random import randint
    int_list = [randint(1, 100) for _ in range(n)]
    return int_list


def create_3d_vector(list1, list2, list3):
    import numpy as np
    vector = np.array([list1, list2, list3])
    return vector


def scalar_product(vector1, vector2):
    import numpy as np
    product = np.dot(vector1, vector2)
    return product


def append_to_list(lst, value):
    lst.append(value)
    return lst

def greater_or_equal_than(a, b):
    result = a>=b
    return result