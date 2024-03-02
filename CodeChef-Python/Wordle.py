t=int(input())
while t>0:
    s=input()
    r=input()
    res=""
    for i in range(0,len(s)):
        if(s[i]==r[i]):
            res+="G"
        else:
            res+="B"
    print(res)  
    t-=1

        

"""like share & Subscribe"""
