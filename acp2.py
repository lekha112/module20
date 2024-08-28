from functools import reduce
import operator

def calculate_product(tup):
    # Use reduce to multiply all elements of the tuple
    return reduce(operator.mul, tup, 1)

# Define the tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate the product for both tuples
product_tup1 = calculate_product(tup1)
product_tup2 = calculate_product(tup2)

# Print the results
print("Product of elements in tup1:", product_tup1)
print("Product of elements in tup2:", product_tup2)
