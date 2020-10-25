a = int(input())
b = int(input())
c = int(input())

res = []
res.append(a)
res.append(b)
res.append(c)

print(max(res))
res.remove(max(res))
print(min(res))
res.remove(min(res))
print(res[0])
