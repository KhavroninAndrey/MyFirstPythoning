x = input()
pi = 3.14
if x == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif x == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
    print(S)
elif x == 'круг':
    r = int(input())
    S = pi * (r ** 2)
    print(S)