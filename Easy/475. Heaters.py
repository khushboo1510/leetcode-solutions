"""
https://leetcode.com/problems/heaters/

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
    1. Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
    2. Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
    3. As long as a house is in the heaters' warm radius range, it can be warmed.
    4. All the heaters follow your radius standard and the warm radius will the same.
"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    
        radius = 0
        houses = sorted(houses)
        heaters = sorted(heaters)
        n = len(heaters)

        i = 0
        flag = False
        for house in houses:
            if house < heaters[i]:
                radius = max(heaters[i] - house, radius)
            else:
                while i + 1 < n:
                    if heaters[i] <= house < heaters[i + 1]:
                        radius = max(radius, min(house - heaters[i], heaters[i + 1] - house))
                        break
                    i += 1
                if i == n - 1:
                    radius = max(radius, house - heaters[i])
        return radius