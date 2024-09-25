t=int(input())
for _ in range(t):
    z,x,c=map(int,input().split())
    max_butterflies=max(z,x,c)
    sum_=0
    sum_= z+ x + c -max_butterflies
    if max_butterflies<=sum_:
        print("YES")
    else:
        print("NO")
