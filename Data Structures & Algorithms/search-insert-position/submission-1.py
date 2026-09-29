class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        - input: given a sorted array and a traget 
        - output: must return the index of the target if found or else must return the index where it would be in place 

        Pattern: binary search 
        time comp: o(log n)

        '''

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return l