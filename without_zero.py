num = 1
for i in range(10):
    n = int(input())
    if n != 0:
        num *= n
    else:
        continue
print(num)