class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_robber_I(houses):
            n = len(houses)
            if n == 1:
                return houses[0]
                
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[n-1]
            
        case1 = house_robber_I(nums[:-1])
        case2 = house_robber_I(nums[1:])

        return max(case1, case2)
        