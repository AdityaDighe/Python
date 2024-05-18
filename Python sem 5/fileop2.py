with open("T1.txt","r") as f1:
    l=[]
    f=f1.read()
    f=f.split()

for line in f:
    l.append(str(line))
    l.sort(key=lambda item:(item,len(item)))
print(l)

with open("T2.txt","w") as f2:
    for i in range(len(l)):
        f2.write(str(l[i]))
        f2.write("\n")


# reversing a word "" List.append(str(line)[::-1])