"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        l = []
        while(n != 1):
           
            if n in l:
                return False
            x = n
            total = 0
            while(n > 9):
                total += (n % 10) ** 2
                n = floor(n / 10)
            total += n ** 2
            if total != 1:
                l.append(x)
            n = total
        return True