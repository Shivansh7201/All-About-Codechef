"""
A an, 
You need to find if there exists any
inter,B which meets the following condition
B must be an integer
B is the average of 
A and C.
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers
A and C, the given integers.
Output Format
For each test case, output 1
−1 if there exists no integer
B such that
A,B, and C are in arithmetic progression. Else, output the value of
B."""

t = int(input())            
for i in range(t):          
    x,c = map(int, input().split())
    if x%2 == 0 and c%2 == 0:
       b = (x+c)//2
       print(b)
    elif x%2 != 0 and c%2 != 0:
        b = (x+c)//2
        print(b)
    else:
        print(-1)
    
