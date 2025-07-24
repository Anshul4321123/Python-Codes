def nrc(s):
  c={}
  for char in s:
    if char in c:
      c[char]+=1
    else:
        c[char]=1
  for char in s:
    if c[char]==1:
      return char 
     


print(nrc("anshulthakur"))