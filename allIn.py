const = int(input())
p = 0
summ = 0
count = 0
count1 = 0
pr = 1
srar = 0
q = 0
num = const
h = const
g = const
f = const
l = const
n = 0
while num != 0:
    p = num % 10
    summ += p
    num = num // 10
print(summ)
while h != 0:
    p = h % 10
    count += 1
    h = h // 10
print(count)
while g != 0:
    p = g % 10
    pr = pr * p
    g = g // 10
print(pr)
while f != 0:
    p = f % 10
    srar += p
    count1 += 1
    f = f // 10
q = srar / count1
print(q)
p = l // (10 ** (count1-1))
print(p)
n = p + (l % 10)
print(n)
