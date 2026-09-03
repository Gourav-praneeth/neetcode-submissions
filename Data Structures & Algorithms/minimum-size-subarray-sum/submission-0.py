class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1
        count = 0
        l = 0

        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                window = r-l+1
                min_length = min(min_length, window)
                count -= nums[l]
                l += 1
                
        if min_length == len(nums) + 1:
            return 0
        return min_length