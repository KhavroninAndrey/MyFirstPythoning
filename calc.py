a = float(input())
b = float(input())
c = input()
x = ''
if c == '+':
    x = a + b
    print(x)
elif c == '-':
    x = a - b
    print(x)
elif c == '/':
    if b != 0:
        x = a / b
        print(x)
    else:
        print('Деление на 0!')
elif c == '*':
    x = a * b
    print(x)
elif c == 'mod':
    if b != 0:
        x = a % b
        print(x)
    else:
        print('Деление на 0!')
elif c == 'pow':
    x = a ** b
    print(x)
elif c == 'div':
    if b != 0:
        x = a // b
        print(x)
    else:
        print('Деление на 0!')

