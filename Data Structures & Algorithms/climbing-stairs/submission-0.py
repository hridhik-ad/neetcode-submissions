class Solution:
    def climbStairs(self, n: int) -> int:
        n += 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1
        
        for i in range(n - 2):
            dp[i + 2] = dp[i + 1] + dp[i]
        return dp[n - 1]
