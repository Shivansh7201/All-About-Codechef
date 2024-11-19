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
#taking input for number of test cases
t=input()
#using a while loop to iterate through each test case
while t&gt;0:
  #taking input for the strings s and t
  s=input()
  t=input()
  #initializing an empty string to store the result
  res=""
  #using a loop to compare characters of s and t at each index
  for i in range(0, len(s)):
    #if characters are equal, add 'G' to the result string
    if(s[i]==t[i]):
      res+="G"
    #if characters are not equal, add 'B' to the result string
    else:
      res+="B"
  #printing the result for the current test case
  print(res)
  t-=1 #decrementing the value of t to move to next test case
