for i in range(int(input())):
    n=int(input())
    d=int(n/4)
    if n%4==0:
        print(d)
    
    elif n<4:
        print(1)
    
    
    elif n>4 and n%4!=0:
        print(d+1)
    
    
   
