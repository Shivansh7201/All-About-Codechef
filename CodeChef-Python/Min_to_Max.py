def min_operations_to_max():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = (input())  # Size of the array
        A = list(map(int, input().split()))  # Array elements

        # Find the minimum value M in the array A
        M = min(A)

        # Count the number of elements in A that are not equal to M
        count = sum(1 for x in A if x != M)

        print(count)

# Example usage
min_operations_to_max()
