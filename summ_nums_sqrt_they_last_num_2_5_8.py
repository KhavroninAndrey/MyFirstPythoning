n = int(input())
nums = 0
for i in range(1, n):
    if ((i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8):
        nums += i
print(nums)