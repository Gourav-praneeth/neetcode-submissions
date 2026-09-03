class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()

        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1



            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    if [nums[i],nums[l],nums[r]] not in lst:
                        lst.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
        return lst


        '''
        U: given a lst of numbers need to output the sum of three numbers which equals to zero and return it in a list will all possible unique triplets.
        I: 
        first i loop: fix one number
            second j loop: take another number starts at (i+1)
                now have a pointer at the end
                check if sum of i+j > 0 or < 0 then move pointers 
                if the sum is zero append it to a lst 
                    also need to check if a possible combination is already to the lst then we should contine. 
        return lst
        '''
