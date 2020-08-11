# https://leetcode.com/problems/excel-sheet-column-number/
    
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# Constraints:
#     - 1 <= s.length <= 7
#     - s consists only of uppercase English letters.
#     - s is between "A" and "FXSHRXW".

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        n = len(s)
        colNum = 0
        for i in range(1, n):
            val = ord(s[i - 1]) - 65
            colNum += pow(26, i) + (val * pow(26, n - i))
            
        return colNum + ord(s[-1]) - 64