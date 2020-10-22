# https://leetcode.com/problems/asteroid-collision/
    
# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        
        while asteroids:
            if not stack:
                stack.append(asteroids.pop(0))
            else:
                if (stack[-1] * asteroids[0] > 0) or (stack[-1] < 0 and asteroids[0] > 0):
                    stack.append(asteroids.pop(0))
                elif -stack[-1] == asteroids[0]:
                    asteroids.pop(0)
                    stack.pop()
                elif abs(stack[-1]) > abs(asteroids[0]):
                    asteroids.pop(0)
                else:
                    stack.pop()
        return stack
