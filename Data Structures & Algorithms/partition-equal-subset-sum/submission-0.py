class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        # [0,1,2,3,4,5,6,7,8,9,10,11]
        # [0,1,0,0,0,0,0,0,0,0,0]
        # [t,t,]
        target = total // 2
    
        # create a dp of size of max elemebt
        dp = [False] * (target+1)
         # base case 
        dp[0] = True

        for num in nums:
            for s in range(target, num-1,-1):
                dp[s] = dp[s] or dp[s-num]

        return dp[target]
