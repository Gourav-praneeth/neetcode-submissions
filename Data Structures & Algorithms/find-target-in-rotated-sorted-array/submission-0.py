class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for num in range(len(nums)):
            if nums[num] == target:
                return num
        return -1