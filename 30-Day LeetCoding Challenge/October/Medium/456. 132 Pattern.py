# https://leetcode.com/problems/132-pattern/solution/
    
# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

# Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        min_arr = [nums[0]]
        
        for num in nums[1:]:
            min_arr.append(min(min_arr[-1], num))
        
        stack, n = [], len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] > min_arr[i]:
                while stack and stack[-1] <= min_arr[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False
