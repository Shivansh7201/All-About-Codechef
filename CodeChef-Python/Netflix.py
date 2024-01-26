t=int(input())

for _ in range(t):

    z,x,c,v=map(int,input().split())

    if((z+x)>=v or (x+c)>=v or (c+z)>=v):

        print("YES")

    else:

        print("NO")



"""like share & Subscribe"""
