class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        - given an array of nums and a target 
        - return the index of target in nums if found or else return -1

        can solve in o(n)
        - must solve in O(log n) therefore we use binary seach

        '''
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r ) // 2 
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            if nums[r] >= nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


        