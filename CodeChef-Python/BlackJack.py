for _ in range(int(input())):
    z,x=map(int,input().split())
    c=21-(z+x)
    if(1<=c<=10):
        print(c)
    else:
        print(-1)

