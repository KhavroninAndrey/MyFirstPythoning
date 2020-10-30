num1 = int(input())
num2 = int(input())
qube = ''
count = 0
for i in range(num1, num2+1):
    qube = i ** 3
    if qube % 10 == 4 or qube % 10 == 9:
        count += 1
    else:
        continue
print(count)