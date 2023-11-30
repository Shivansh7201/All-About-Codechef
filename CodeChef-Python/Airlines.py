def min_p(X, N):
    plane= (N//100)+ (1 if N % 100 !=0 else 0 )
    
    additional_p = plane - X
    
    return max(0, additional_p)
    
T= int(input())

for _ in range(T):
    X,N = map(int,input().split())
    
    result=min_p(X,N)
    
    print(result)
