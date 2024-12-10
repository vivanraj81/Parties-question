# 1498. Number of Subsequences That Satisfy the Given Sum Condition

nums.sort()
n = len(nums)
res = 0
mod = 10 ** 9 + 7

if nums[0] > target:
    return 0

for i in range(n):
    j = bisect.bisect(nums, target-nums[i]) - 1
    if j >= i:
        res += pow(2, j - i, mod)
    else:
        break
return res % mod