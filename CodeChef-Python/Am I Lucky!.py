for _ in range(int(input())):
    mp,mb,gm= map(int,input().split())
    gh=mp-mb
    brt=mb%gm
    gre=gh%gm
    maximum=max(brt,gre)
    minimum=min(brt,gre)
    print(maximum-minimum)
    
