# cook your dish here
for i in range(int(input())):
    N,X = map(int, input().split(' '))
    if X>=N and X%N == 0:
        print('YES')
    else:
        print('NO')
