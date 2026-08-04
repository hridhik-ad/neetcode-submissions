
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Edge cases: 0 or 1 house
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
            
        # We only need an array of size n because the "top" is the last house
        dp = [0] * n
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Build the max profit bottom-up
        for i in range(2, n):
            # Choice: skip this house (dp[i-1]) OR rob this house (dp[i-2] + nums[i])
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        # The last element holds the maximum profit
        return dp[-1]