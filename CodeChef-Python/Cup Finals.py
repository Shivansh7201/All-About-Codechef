# cook your dish here
n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    d=abs(a-b)
    if(d<=c):
        print("YES")
    else:
        print("NO")
