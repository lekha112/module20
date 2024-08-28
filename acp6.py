import random
import string

def generate_random_password(length):
    # Define the characters to include in the password
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    all_characters = lower_case + upper_case + digits
    
    # Generate a random password
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Create the password by randomly choosing characters
    password = [random.choice(all_characters) for _ in range(length)]
    
    # Shuffle the generated password to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

# Get user input for the password length
try:
    length = int(input("Enter the desired length of the password: "))
    password = generate_random_password(length)
    print("Generated Password:", password)
except ValueError as e:
    print("Invalid input:", e)
