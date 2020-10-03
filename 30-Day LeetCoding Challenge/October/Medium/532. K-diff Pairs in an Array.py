# https://leetcode.com/problems/k-diff-pairs-in-an-array/
    
# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# - 0 <= i, j < nums.length
# - i != j
# - a <= b
# - b - a == k

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        nums = set(nums)
        count = 0
        if k == 0:
            for num in nums:
                if d[num] > 1:
                    count += 1
        else:
            for num in nums:
                if k + num in d:
                    count += 1
        return count
