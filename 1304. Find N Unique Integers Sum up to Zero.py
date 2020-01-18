import math

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        lst = []
        if n % 2 != 0:
            for x in range(0,n):
                lst.append(x-math.floor(n/2))
        else:
            for x in range(0,n+1):
                value = x - math.floor(n/2)
                if value != 0:
                    lst.append(value)
        return lst