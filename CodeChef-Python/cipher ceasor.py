"""This problem can be solved by finding the shift between the first character of S and T, 
and then applying the same shift to U. The shift can be found by subtracting the ASCII 
value of the first character of S from the ASCII value of the first character of T.
 If the result is negative, we add 26 to it to make it positive. We then add the shift to each character of U,
   modulo 26 to handle the circular shift."""
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    t = input()
    u = input()
    shift = (ord(t[0]) - ord(s[0]) + 26) % 26
    result = ''
    for char in u:
        result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    print(result)

"""This script first reads the number of test cases. For each test case, it reads the length of the strings, and the strings S, T, and U.
 It then calculates the shift and applies it to each character of U, modulo 26 to handle the circular shift. The result is the ROT-K cipher of U."""    