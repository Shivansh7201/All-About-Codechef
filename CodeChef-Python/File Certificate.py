def max_present_days(n, s):
    max_present = s.count('1')
    max_present_with_op = max_present
    
    for i in range(n):
        if s[i] == '0':
            j = i
            while j < n and s[j] == '0':
                j += 1
            max_present_with_op = max(max_present_with_op, j - i + max_present)
            
    return max_present_with_op
    
T=int(input())
for _ in range(T):
    n= int(input())
    s= input().strip()
    print(max_present_days(n, s))
    

            
            
