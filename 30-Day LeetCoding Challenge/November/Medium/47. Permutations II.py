# https://leetcode.com/problems/permutations-ii/submissions/
    
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.n = len(nums)
        nums.sort()
        def backtrack(arr, path, m):
            if not arr:
                self.result.append(path)
            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                backtrack(arr[:i] + arr[i+1:], path + [arr[i]], m + 1)
        
        backtrack(nums, [], 0)
        
        return self.result
