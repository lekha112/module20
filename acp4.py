# Define the sets
set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}

set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}

# Calculate symmetric differences
symmetric_diff_a = set1_a.symmetric_difference(set2_a)
symmetric_diff_b = set1_b.symmetric_difference(set2_b)

# Print the results
print("Symmetric Difference between Set1 and Set2 for Example A:", symmetric_diff_a)
print("Symmetric Difference between Set1 and Set2 for Example B:", symmetric_diff_b)
