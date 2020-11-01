num = int(input())
count = 0
while num >= 25:
    num -= 25
    count += 1
while num >= 10:
    num -= 10
    count += 1
while num >= 5:
    num -= 5
    count += 1
while num >= 1:
    num -= 1
    count += 1
print(count)