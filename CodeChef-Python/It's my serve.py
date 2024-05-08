# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    c=x+y
    b=c//2
    if(b%2==0 ):
        print("Alice")
    else:
        print("bob")
