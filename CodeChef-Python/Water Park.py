"""The first and only line of input will contain two space-separated integers 

W and H. """

x,c=map(int,input().split())
if x>=60 and c<=130:
    print("YES")
else:
    print("NO")

""" Chef is allowed on the water slide, because:

His height is 
130
130 cm, which is 
≥
110
≥110.
His weight is 
60
60 kg, which is 
≤
75
≤75. """

"""
# Chef's height is 
≥
115
≥115 cm, but his weight is greater than 
55
55 kg.
So, Chef is NOT allowed on the water slide."""
