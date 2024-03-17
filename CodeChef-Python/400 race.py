t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if((400/x)>(400/y) and (400/x)>(400/z)):
        print("ALICE")
    elif((400/y)>(400/x) and (400/y)>(400/z)):
        print("BOB")
    else:
        print("CHARLIE")
