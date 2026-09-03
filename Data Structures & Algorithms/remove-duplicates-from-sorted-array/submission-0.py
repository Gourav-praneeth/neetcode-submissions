class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        
        for r in range(1,len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1 
        return l + 1

            
