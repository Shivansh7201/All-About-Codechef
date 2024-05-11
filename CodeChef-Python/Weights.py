for _ in range(int(input())):
    w,e,r,t=map(int,input().split())
    s={e,r,t,e+r,e+t,r+t,e+r+t}
    print('yes' if w in s else 'no')
    


"""like share & Subscribe"""
