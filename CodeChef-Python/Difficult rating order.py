

def check_order_of_difficulty(n, difficulties):

    for i in range(1, n):

        if difficulties[i - 1] > difficulties[i]:

            return "No"

    return "Yes"





t = int(input().strip())



for _ in range(t):

 

    n = int(input().strip())

    difficulties = list(map(int, input().strip().split()))



    result = check_order_of_difficulty(n, difficulties)

    print(result)

    
