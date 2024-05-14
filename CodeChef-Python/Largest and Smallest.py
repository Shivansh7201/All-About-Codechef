t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    m1,m2=max(a),0
    for x in a:
        if x!=m1:m2=max(m2,x)
    print(m1+m2)    
    t -= 1
# Your code goes here
