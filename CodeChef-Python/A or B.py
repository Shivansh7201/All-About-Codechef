# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    ans1=500-2*x+1000-4*(x+y)
    ans2=500-2*(x+y)+1000-4*y
    
    a=max(ans1,ans2)
    print(a)

