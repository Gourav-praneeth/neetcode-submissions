class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        - input: given an arraqy of nums
        - return [i,j,k] where their sum is equal to zero 
        '''

        res = []
        nums.sort()
        
        for i in range(len(nums)):
            #skips i dulpicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i+1
            r = len(nums) - 1

            

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r -= 1

                    # skip duplicates for left
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    # skip duplicates for right
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res



        # brute force O(n^3)
        # res = []

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if triplet not in res:
        #                     res.append(triplet)

        # return res

        # optimial solution using two pointer
