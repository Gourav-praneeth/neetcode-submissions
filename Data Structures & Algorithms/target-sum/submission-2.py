class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        offset = total

        dp = [0] * (2*total + 1)
        if abs(target) > total:
            return 0


        dp[offset] = 1

        for num in nums:
            new_dp = [0] * (2*total +1)

            for s in range(-total, total+1):
                if dp[s+offset] > 0:
                    new_dp[s + num + offset] += dp[s+offset]
                    new_dp[s - num + offset] += dp[s+offset]
            dp = new_dp

        return dp[target + offset]