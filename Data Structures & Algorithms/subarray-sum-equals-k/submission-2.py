class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        input - given an array of numbers and a target sum value
        output - return the count of subarray sums that the array have or can make 

        p:
        - have a variable window 
        - start with the value and increase the window until you see the target value and if it exceeds the vale remove the first value in the window and continue 
        - if you see the summ == target we increment the count by 1
        - time complexity would be o(n) since we are using sliding window technique and have 1 loop
        - space woukld be o(1) since we are just comparing not creating additional space

        '''
        # brute force
        # count = 0
        # for i in range(len(nums)):
        #     curr_sum = 0

        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]

        #         if curr_sum == k:
        #             count += 1
        # return count

        # optimal solution 
        # count = 0
        # curr_sum = 0
        # prefix_count = {0 : 1} # 2: 0

        # for num in nums:
        #     curr_sum += num

        #     need = curr_sum - k

        #     if need in prefix_count:
        #         count += prefix_count[need]

        #     if curr_sum in prefix_count:
        #         prefix_count[curr_sum] += 1
        #     else:
        #         prefix_count[curr_sum] = 1

        # return count

        count = 0
        curr_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            curr_sum += num

            need = curr_sum - k

            if need in prefix_count:
                count += prefix_count[need]

            if curr_sum not in prefix_count:
                prefix_count[curr_sum] = 1
            else:
                prefix_count[curr_sum] += 1

        return count



