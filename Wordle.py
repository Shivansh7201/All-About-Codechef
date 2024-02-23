t=intput()
while t>0:
  s=input()
  t=input()
  res=""
  for i in range(0, len(s)):
    if(s[i]==t[i]):
      res+="G"
    else:
      res+="B"
  print(res)
  t-=1
