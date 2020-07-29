import re

def checkTraffic(cost,traffic):
    if traffic == 'heavy\n':
        cost = cost*1.2
    elif traffic == 'light':
        cost = cost*0.8
    cost=int(cost)
    print(cost)
    return cost
f = open("example.txt", "r")
f=f.readlines()
arr=[]
for line in f:
    if re.match("^(n|N)[0-9]+$", line):
        continue
    else:
        (var1, var2, var3, var4) = line.split(",")
        var3=int(var3)
        cost=checkTraffic(var3,var4)
        arr.append((var1,var2,cost))
print(arr)    
    