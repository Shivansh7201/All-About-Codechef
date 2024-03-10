for i in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for j in a:
        if 9<j<61:
            count+=1
    print(count)
  
