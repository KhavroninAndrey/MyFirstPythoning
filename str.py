x = input()
d = len(x)
f = 0
for i in x.lower():
    if i == 'g':
        f += 1
    elif i == 'c':
        f +=1
h = (f / d) * 100
print(h)