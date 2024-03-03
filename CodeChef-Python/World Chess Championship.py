t = int(input())
for _ in range(t):
    x = int(input())
    p = input()
    c = 0
    n = 0
    d = 0
    for i in range(0,len(p)):
        if p[i] == "C":
            c+=1
        elif p[i] == "N":
            n+=1
        elif p[i] == "D":
            d+=1
    cr = (2*c)+(d*1)
    nr = (2*n)+(1*d)
    if cr == nr:
        print(55 * x)
    elif cr > nr:
        print(x*60)
    else:
        print(x*40)
        
