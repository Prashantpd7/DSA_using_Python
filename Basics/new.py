# Question (easy)
# Write a function sum_even(nums) that takes a list of integers and returns the sum of all even
# numbers. Example: sum_even([1, 2, 3, 4]) returns 6.

# Hint
# Iterate through the list and add numbers to a total only if they are divisible by 2.

def sum_even(nums): # Define a function that takes a list of integers
    """
    Takes a list of integers and returns the sum of all even numbers.
    """
    total = 0 # Initialize a variable to store the running sum
    for num in nums: # Loop through each number in the list
        if num % 2 == 0: # Check if the number is divisible by 2 (even)
            total += num # Add the even number to the total
    return total # Return the final sum of all even numbers

# Execution block
# Explanation:
# This code defines a function that loops through a list, adds only the even numbers to a running total, and returns the final sum. The `if` statement checks if a number is even before adding it.
if __name__ == "__main__": # Check if the script is run directly
    # Test case 1
    result = sum_even([1, 2, 3, 4]) # Call the function with test data
    print(f"sum_even([1, 2, 3, 4]) = {result}")  # Expected: 6
    
    # Test case 2
    result = sum_even([10, 15, 20, 25]) # Call the function with test data
    print(f"sum_even([10, 15, 20, 25]) = {result}")  # Expected: 30
    
    # Test case 3 (empty list)
    result = sum_even([]) # Call the function with an empty list
    print(f"sum_even([]) = {result}")  # Expected: 0
