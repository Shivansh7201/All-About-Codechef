t = int(input())

while t > 0:
    n, x = map(int, input().split())
    total_bill = n * x
    if total_bill >= 10000 and total_bill <= 99999:
        print("YES")
    else:
        print("NO")
        
    t -= 1