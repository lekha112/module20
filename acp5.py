# Get user input
try:
    number = int(input("Enter a number: "))
    
    # List comprehension to create a list of odd numbers below the input value
    odd_numbers_below = [x for x in range(number) if x % 2 != 0]
    
    # List comprehension to create a list of odd numbers above a certain threshold (e.g., 10)
    threshold = 10
    odd_numbers_above_threshold = [x for x in range(threshold + 1, number) if x % 2 != 0]
    
    # Print the results
    print("Odd numbers below", number, ":", odd_numbers_below)
    print("Odd numbers above", threshold, "and below", number, ":", odd_numbers_above_threshold)
    
except ValueError:
    print("Please enter a valid integer.")
