t=int(input())
y=list(map(int,input().split())
ev=0
od=0
for i in y:
  if i%2==0:
    ev+=1
  else:
    od+=1
if ev>od:
  print("READY FOR BATTLE")
else:
  print("NOT ENOUGH")
    
