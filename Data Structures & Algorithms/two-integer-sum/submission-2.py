class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        - given an array and a target 
        - return the index of two numbers which equals to the target sum
        '''

        # o(n^2) solution

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]