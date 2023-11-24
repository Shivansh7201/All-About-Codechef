"""We know that "A picture is worth a thousand words". So let's calculate the worth of a video using this!

Suppose a video has 24 frames (or pictures) per second, and has a duration of 
�
S seconds. We know that each frame is worth 
1000
1000 words. So, how many words is this video worth in total?"""
# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    x=x*24
    print(x*1000)