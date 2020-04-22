"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_num = 0
        sum_map = defaultdict(list)
        sum_map[0].append(-1) # Initialize the first 0
        max_len = 0
        # Calculate sum for each position, and put positions together if they have the same sum, which means 0s             and 1s are the same between those positions.
        for i in range(len(nums)):
            if nums[i] == 0:
                sum_num -= 1
            else:
                sum_num += 1
            sum_map[sum_num].append(i)
        # Compare and get max interval    
        for k,v in sum_map.items():
            v.sort()
            if v[-1] - v[0] > max_len:
                max_len = v[-1] - v[0]
        return max_len