# Define the test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:", test_dict)

# Ask the user to enter a value to check the frequency
try:
    # Read user input
    user_value = int(input("Enter the value to check its frequency: "))

    # Calculate frequency of the entered value
    frequency = list(test_dict.values()).count(user_value)

    # Print the frequency
    print(f"The frequency of the value {user_value} is: {frequency}")

except ValueError:
    print("Please enter a valid integer value.")
