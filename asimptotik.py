import math
n = int(input())
num = 1
for i in range(n):
    num = num + (1/i)
result = num - math.log(n)
print(result)