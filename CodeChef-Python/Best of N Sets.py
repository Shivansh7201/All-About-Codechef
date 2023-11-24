"""Sonu and Titu are playing a tennis match. They are playing a "best of 
�
N sets" match (
�
N is always odd). That means that they will play at most 
�
N sets, and the person who has won most sets wins the match. But they are smart, and if they notice at any point that one of them has no chance of winning the match, they will stop the match right then, without playing out all the 
�
N sets needlessly.

For example, suppose 
�
=
11
N=11. And at some point, Sonu has won 5 sets, and Titu has won 4 sets. Sonu is leading now, but it is possible that Titu wins the two remaining sets and wins the whole match. So they will not stop right now.

But suppose Sonu wins the next set as well, and so now the score is 
(
6
,
4
)
(6,4). Now, even though there is one set remaining, there is no chance of Titu winning the whole match, since at best, even if he wins the next set, the score will become 
(
6
,
5
)
(6,5), and Sonu still wins. So, they will stop at a score of 
(
6
,
4
)
(6,4) and declare Sonu as the winner."""

def find(X, Y):
    diff = abs(X - Y)
    total_S= X + Y
    N= total_S + diff
    if N %2 ==0:
        N-=1
    
    return N

def main():
    T=int(input())
    for _ in range(T):
        X, Y= map(int,input().split())
        N =find(X, Y)
        print(N)
        
if __name__ =="__main__":
    main()
        