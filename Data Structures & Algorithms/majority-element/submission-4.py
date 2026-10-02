class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        majority = nums[0]

        for num in count:
            if count[num] > count[majority]:
                majority = num
        return majority