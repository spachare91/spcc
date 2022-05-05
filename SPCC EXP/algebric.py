def asm(code):
  code1=[]
  for i in code:
    if "+0" in i:
      i=i.replace("+0","")
    if "*1" in i:
      i=i.replace("*1","")
    code1.append(i)
  for i in code1:
    i=i.split("=")
    if(i[0]==i[1]):
      continue
    print(i[0]+"="+i[1])
    
n=int(input("Enter number:"))
code=[]
for _ in range(n):
  s=input("Enter line:")
  code.append(s)
asm(code)