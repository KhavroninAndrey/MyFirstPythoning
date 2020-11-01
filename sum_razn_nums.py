n = int(input())
nums = 0
for i in range(1, n+1):
    nums += (i * (-1)**(i+1))
print(nums)