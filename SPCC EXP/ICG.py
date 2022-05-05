exp = input("Enter the expression: ")
x = exp.split(" ")
counter = 1
y = x 
for i in range(len(y)):
    if y[i].isalpha():
        y[i] = "id" + str(counter)
        counter += 1
    print(y[i])


no_temp = counter - 2
temp1 = ""

for i in range(3):
    temp1 += str(y[i]) + " "

z="temp1 = " + temp1
z=z.split(" ")

print("OP\t ARG1 \tARG2\t RES")
print(f"{z[3]}\t {z[2]}\t {z[4]}\t {z[0]}")

temp = []
for z in range(no_temp):
    res = "temp" + str(z+1)
    temp.append(res)
#print("temp: ",temp)
#print(y)
i = 1
req=[]
for k in range(3, len(y), 2):
    ans = ""
    ans = temp[i] + " = " + temp[i-1]+" " + y[k]+" " + y[k+1]
    i = i + 1
    req.append(ans)


for x in range(len(req)):
    z=req[x].split(" ")
    print(f"{z[3]}\t {z[2]}\t {z[4]}\t {z[0]}")