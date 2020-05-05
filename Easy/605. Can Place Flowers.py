"""
https://leetcode.com/problems/can-place-flowers/

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed = [0] + flowerbed + [0]
        m = len(flowerbed)
        
        for i in range(1, m - 1):
            
            if n < 1:
                break
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and i + 1 <= m - 1 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n == 0