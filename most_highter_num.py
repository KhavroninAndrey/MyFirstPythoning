n = int(input())
p = 0
l = 0
for i in range(n):
    num = int(input())
    if num > p and num > l:
        p = l
        l = num
    elif p< num < l:
        p = num
print(l)
print(p)