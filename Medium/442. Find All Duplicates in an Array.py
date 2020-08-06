# https://leetcode.com/problems/find-all-duplicates-in-an-array/
    
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
       
        i, result = 0, {}
        while i < len(nums):
            if i != nums[i] - 1:
                if nums[i] == nums[nums[i] - 1]:
                    result[nums[i]] = nums[i]
                else:
                    temp = nums[i]
                    nums[i] = nums[temp - 1]
                    nums[temp - 1] = temp
                    i -= 1
            i += 1
                
        return result.keys()