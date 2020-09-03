# https://leetcode.com/problems/largest-time-for-given-digits/
    
# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        perms = itertools.permutations(A)

        for a,b,c,d in sorted(perms, reverse = True):
            if (a == 2 and b <= 3 and c <= 5) or (a <= 1 and b <= 9 and c <= 5):
                return '{}{}:{}{}'.format(a, b, c, d)
            
        return ''