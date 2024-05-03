t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if n<4 or m<4:
        print(-1)
    else:
        a.sort(reverse=True)
        b.sort(reverse=True)
        top_bats=a[:7]
        top_bowls=b[:7]
        combined_skills=top_bats+top_bowls
        combined_skills.sort(reverse=True)
        if len(combined_skills)<11:
            print(-1)
        else:
            max_skill=sum(combined_skills[:11])
            print(max_skill)
            
        
    

"""Fork share & Follow"""
