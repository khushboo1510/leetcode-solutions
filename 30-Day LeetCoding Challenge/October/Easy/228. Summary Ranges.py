# https://leetcode.com/problems/summary-ranges/
    
# You are given a sorted unique integer array nums.

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:
#     - "a->b" if a != b
#     - "a" if a == b

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        
        res = [[nums[0]]]
        
        for i, num in enumerate(nums[1:], 1):
            if num == nums[i - 1] + 1:
                res[-1].append(num)
            else:
                res.append([num])
        result = []
        for r in res:
            if r[0] == r[-1]:
                result.append(str(r[0]))
            else:
                result.append(str(r[0]) + "->" + str(r[-1]))
                
        return result
