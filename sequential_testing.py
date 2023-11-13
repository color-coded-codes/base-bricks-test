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


def generate_random_words(reference_text, n):
    import random
    # Split the reference text into words
    words = reference_text.split()

    # Ensure n is non-negative
    n = max(n, 0)

    # Generate the new text by randomly selecting words
    generated_words = [random.choice(words) for _ in range(n)]

    # Combine the generated words into a text
    generated_text = ' '.join(generated_words)

    return generated_text


def generate_random_text(n):
    import random
    import string
    
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_text = ''.join(random.choice(characters) for _ in range(n))
    
    return random_text


def generate_random_integer(min_value, max_value):
    import random
    
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

