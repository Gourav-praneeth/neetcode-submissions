class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= suffix
            suffix = suffix * nums[i]

        return res
        # n = len(nums)
        # left_prod = [1] * n
        # right_prod = [1] * n
        # res = [0] * n

        # for i in range(1,n):
        #     left_prod[i] = left_prod[i-1] * nums[i-1]

        # for i in range(n-2,-1,-1):
        #     right_prod[i] = right_prod[i+1] * nums[i+1]

        # for i in range(n):
        #     res[i] = left_prod[i] * right_prod[i]
        
        # return res