class Solution:
    def isPalindrome(self, x: int) -> bool:
        xReverse = str(x)[::-1]
        return str(x) == xReverse