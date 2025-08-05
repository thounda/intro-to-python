# Write your code here

# HINT: create a dictionary from flowers.txt

# HINT: create a function to ask for user's first and last name


# print the desired output

def read_flowers_to_dict(flowers_data_string):
    """
    Reads flower data from a string and saves it as a dictionary.
    The dictionary keys are the first letters of the flower names,
    and the values are the full flower names.

    Args:
        flowers_data_string (str): A string containing flower data,
                                   where each line is in the format "Letter: Flower Name".

    Returns:
        dict: A dictionary mapping first letters to flower names.
    """
    flowers_dict = {}
    lines = flowers_data_string.strip().split('\n')
    for line in lines:
        if ':' in line:
            # Split by the first colon only to handle flower names with colons
            key, value = line.split(':', 1)
            # Strip whitespace from key and value and store in dictionary
            flowers_dict[key.strip().upper()] = value.strip()
    return flowers_dict

def match_flower_to_name(flowers_dict):
    """
    Takes user input for their first and last name, parses it to find
    the first letter of the first name, and then prints the flower name
    from the dictionary that starts with the same letter.

    Args:
        flowers_dict (dict): A dictionary mapping first letters to flower names.
    """
    while True:
        try:
            full_name = input(">>> Enter your First [space] Last name only: ").strip()
            if not full_name:
                print("Name cannot be empty. Please try again.")
                continue

            # Split the full name into parts
            name_parts = full_name.split()

            if len(name_parts) < 2:
                print("Please enter both your first and last name, separated by a space.")
                continue

            first_name = name_parts[0]
            if not first_name.isalpha():
                print("First name should contain only alphabetic characters. Please try again.")
                continue

            first_letter = first_name[0].upper()

            if first_letter in flowers_dict:
                print(f">>> Unique flower name with the first letter: {flowers_dict[first_letter]}")
                break # Exit loop on successful match
            else:
                print(f"No flower found starting with the letter '{first_letter}'. Please try again with a different name.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    # Create the dictionary from the provided flower data
    flower_names_dict = read_flowers_to_dict(FLOWERS_DATA)

    # Call the function to get user input and display the matching flower
    match_flower_to_name(flower_names_dict)
