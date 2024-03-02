# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the length of the binary string (this variable isn't used but necessary to match input format)
    n = int(input())
    # Read the binary string
    s = input()

    # Initialize the count of operations needed to 0
    operations = 0
    
    # Iterate over the string to find consecutive similar characters
    for i in range(n-1): # n-1 because we are checking the current and next character
        if s[i] == s[i+1]: # If two consecutive characters are the same
            operations += 1 # Increment the count of operations

    # Print the total operations needed for the current test case
    print(operations)
