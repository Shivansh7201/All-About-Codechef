"""Harsh was recently gifted a book consisting of
N pages. Each page contains exactly
M words printed on it. As he was bored, he decided to count the number of words in the book.

Help Harsh find the total number of words in the book."""

T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    print(n*m)