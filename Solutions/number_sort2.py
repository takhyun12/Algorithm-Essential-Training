N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))

nums = sorted(nums)

for num in nums:
    print(num)