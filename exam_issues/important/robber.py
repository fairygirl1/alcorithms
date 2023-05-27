def rob(nums):
    if len(nums) == 1: return nums[0]
    dp = [0] * len(nums)
    dp[0], dp[1] = nums[0], max(nums[:2])
    for k in range(2, len(dp)):
        dp[k] = max(
            dp[k-1],
            dp[k-2] + nums[k]
        )
    return dp[-1]
print(rob([2,7,9,3,1]))