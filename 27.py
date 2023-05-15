f = open("27A_7881.txt")
n = int(f.readline())
k = int(f.readline())

c = 0
a = [int(i) for i in f]
for i in range(len(a) - k):
    for j in range(i + 1, i + k + 1):
        if abs(a[i] - a[j]) % 100 == 0:
            if a[i] % 37 == 0 or a[j] % 37 == 0:
                c += 1

print(c)
