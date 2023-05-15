f = open("grob.txt")

a = [int(i) for i in f]

s = 0
for i in a:
    i1 = str(i)
    for j in i1:
        s += int(j)

print(s)