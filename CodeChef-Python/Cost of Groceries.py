t = int(input()) 

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total_cost = 0
    for i in range(n):
        if a[i] >= x:
            total_cost += b[i]
    print(total_cost)
    t -= 1
