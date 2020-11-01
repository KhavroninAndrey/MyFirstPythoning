n = int(input())
num_summ = 0
for i in range(1, n+1):
    if n % i == 0:
        num_summ += i
print(num_summ)