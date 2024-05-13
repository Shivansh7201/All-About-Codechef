for _ in range(int(input())):
    z,x,c,v=map(int,input().split())
    n=z-x-c
    if n>=v:
        print("0")
    elif z-min(x,c)>=v:
        print("1")
    else:
        print("2")


"""like share & Subscribe"""
