class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and bin(n).count('1') == 1:
            return True
        return False