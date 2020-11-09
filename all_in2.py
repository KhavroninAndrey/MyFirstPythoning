num = int(input())
n = num
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
last_digit = num % 10
while n > 0:
    if n % 10 == 3:
        counter1 += 1
        n = n // 10
    else:
        n = n // 10
print(counter1)
n = num
while n > 0:
    if n % 10 == last_digit:
        counter2 += 1
        n = n // 10
    else:
        n = n // 10
print(counter2)
n = num
while n > 0:
    if n % 2 == 0:
        counter3 += 1
        n = n // 10
    else:
        n = n // 10
print(counter3)
n = num
f = 0
while n > 0:
    f = n % 10
    if f > 5:
        counter4 += f
        n = n // 10
    else:
        n = n // 10
print(counter4)
n = num
counter5 = 1
while n > 0:
    f = n % 10
    if f > 7:
        counter5 *= f
        n = n // 10
    else:
        n = n // 10
print(counter5)
n = num
counter6 = 0
while n > 0:
    f = n % 10
    if f == 0 or f == 5:
        counter6 += 1
        n = n // 10
    else:
        n = n // 10
print(counter6)