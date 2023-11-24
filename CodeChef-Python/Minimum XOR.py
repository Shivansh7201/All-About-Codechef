"""You have 
�
N integers - 
�
1
,
�
2
,
…
,
�
�
A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 .

You have to make the Bitwise XOR of all the elements as minimum as possible.

You are allowed to remove at most one element. Note that this means that you can also choose to not remove any element.

What is the final minimum XOR that you can achieve after removing at most one element?

Note: In most programming languages, the XOR of two variables x and y can be computed using x ^ y."""

# cook your dish here
def min_xor(n,arr):
    
    xor =0
    
    for num in arr:
        xor ^=num
        
    min_xor = xor
    for num in arr:
        temp_xor =xor ^ num
        min_xor= min(min_xor, temp_xor)
    return min_xor
t= int(input()) 
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    result = min_xor(n,arr)
    print(result)