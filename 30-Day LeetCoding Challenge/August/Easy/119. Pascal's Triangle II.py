# https://leetcode.com/problems/pascals-triangle-ii/
    
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

# Follow up:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        dp = [1]
        
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                dp[j] += dp[j - 1]
            dp.append(1)
        return dp