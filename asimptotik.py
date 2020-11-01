import math
n = int(input())
num = 1
for i in range(2, n+1):
    num = num + (1/i)
result = num - math.log(n)
print(result)