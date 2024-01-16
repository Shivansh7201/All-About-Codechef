# Function to check if the problems are attempted in non-decreasing order of difficulty rating
def check_order_of_difficulty(n, difficulties):
    for i in range(1, n):
        if difficulties[i - 1] > difficulties[i]:
            return "No"
    return "Yes"

# Input the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    # Input the number of problems and difficulty ratings
    n = int(input().strip())
    difficulties = list(map(int, input().strip().split()))

    # Check and print the result for the current test case
    result = check_order_of_difficulty(n, difficulties)
    print(result)
