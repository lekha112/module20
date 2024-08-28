def square_and_filter(start, end):
    # Check if the provided range is valid
    if start > end:
        print("Invalid range: start should be less than or equal to end.")
        return
    
    # Lists to store squared values
    squared_values = []
    
    # Calculate the square of each number in the range
    for number in range(start, end + 1):
        squared_value = number ** 2
        squared_values.append(squared_value)
    
    # Separate the squared values into odd and even
    even_squares = [value for value in squared_values if value % 2 == 0]
    odd_squares = [value for value in squared_values if value % 2 != 0]
    
    # Print the results
    print("Squared values:")
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

# Example usage:
square_and_filter(1, 10)
