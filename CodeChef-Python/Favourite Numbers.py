t = int(input())

while t > 0:
    a = int(input())
    if(a%7==0 and a%2==0 ):
        print("Alice")
    elif(a%9==0 and a%2!=0):
        print("Bob")
    else:
        print("Charlie")
        
    t -= 1
