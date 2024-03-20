def main():
  t=int(input())
  while(t>0):
    z,x=map(int,input().split())
    a=list(map(int,input().split()))
    count = 0
    for i in range(n):
      if(a[i]>= x):
        count += 1
    print(count)
    t-=1
if __name__ = "__main__":
  main()

    
