import re
f = open("example.txt", "r")
f=f.readlines()
arr=[]
for line in f:
    if re.match("^(n|N)[0-9]+$", line):
        continue
    else:
        (var1, var2, var3, var4) = line.split(",")
        var3=int(var3)
        arr.append((var1,var2,var3,var4))
print(var3)
print(arr)    
    