a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 < a2 and b2 < b1:
    print(a2, b2)
elif a1 < a2 and b2 == b1:
    print(a2, b2)
elif a1 == a2 and b2 < b1:
    print(a2, b2)
elif a1 == a2 and b1 == b2:
    print(a2, b2)
elif a2 == a1 and b1 < b2:
    print(a1, b1)
elif a2 < a1 and b1 == b2:
    print(a1, b1)
elif a2 < a1 and b1 > b2:
    print(a1, b1)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
elif a1 < b1 == a2 < b2:
    print(b1)
elif a2 < b2 == a1 < b2:
    print(b2)
elif a1 < b1 < a2 < b2 or a2 < b2 < a1 < b1:
    print('пустое множество')