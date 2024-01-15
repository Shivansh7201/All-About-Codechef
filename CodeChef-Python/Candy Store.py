def candy_store(x,y):
  if(x>=y):
    print(y*1)
  else:
    print(x + (y- x)*2)

t=int(input())
for _ in range(t):
  x,y=map(int,input().split())
  candy_store(x,y)
