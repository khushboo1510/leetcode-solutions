class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        n = len(s)
        left = 0
        right = 0
        for element in shift:
            
            if element[0] == 0:
                left += element[1]
            else:
                right += element[1]
                
        diff = (left - right) % n
        
        return s[diff:] + s[:diff]