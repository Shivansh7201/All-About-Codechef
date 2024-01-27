# cook your dish here
t = int(input())
i = 0
while i < t:
    n, x = map(int, input().split(' '))
    if n < 6:
        print(x)
    else:
        if n % 6 == 0:
            print(int((n / 6) * x))
        else:
            n = int(n / 6)
            n = n + 1
            print(n * x)
    i = i + 1
