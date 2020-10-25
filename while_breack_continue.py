i = 0
while i < 5:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        print(a)
    i += 1