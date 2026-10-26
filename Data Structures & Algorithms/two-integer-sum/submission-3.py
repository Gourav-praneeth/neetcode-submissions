class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for num in range(len(nums)):
            complement = target - nums[num]
            if complement not in seen:
                seen[nums[num]] = num
            else:
                return [seen[complement], num]