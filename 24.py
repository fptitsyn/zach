f = open("24.txt")

a = f.read().split()
c = 0
for i in a:
    if "Q" in i:
        qind = i.index("Q")
        if "W" in i[qind::]:
            wind = i[qind::].index("W") + qind
            if "E" in i[wind::]:
                eind = i[wind::].index("E") + wind
                if "R" in i[eind::]:
                    rind = i[eind::].index("R") + eind
                    if "T" in i[rind::]:
                        tind = i[rind::].index("T") + rind
                        if "Y" in i[tind::]:
                            yind = i[tind::].index("Y") + tind
                            c += 1
print(c)
