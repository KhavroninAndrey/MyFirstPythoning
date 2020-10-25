s = 0
u = 0
a = int(input())
b = int(input())
for i in range (a, b+1):
    if i % 3 == 0:
        s += 1
        u += i
    else:
        i += 1
        continue
print(u/s)