"""Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

Minimum age limit is 
�
X (i.e. Age should be greater than or equal to 
�
X).
Age should be strictly less than 
�
Y.
"""

t = int(input())           
for i in range(t):
    x, y, a = map(int, input().split())
    if a>= x and a<y:
        print("YES")
    else:
        print("NO")
