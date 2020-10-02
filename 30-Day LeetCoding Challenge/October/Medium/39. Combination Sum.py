# https://leetcode.com/problems/combination-sum/
    
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.result = []
        candidates.sort()
        
        def traverse(total, candidates, combination):
            if total == target:
                self.result.append(combination)
                return
            
            for i, candidate in enumerate(candidates):
                if total + candidate > target:
                    return
                traverse(total + candidate, candidates[i:], combination + [candidate])
                
        traverse(0, candidates, [])
        return self.result
