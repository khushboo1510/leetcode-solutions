# https://leetcode.com/problems/robot-bounded-in-circle/
    
# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        vector, direction = [0, 0], 'N'
        d = {'N' : [[0, 1], 'W', 'E'], 'W' : [[-1, 0], 'S', 'N'], 'S' : [[0, -1], 'E', 'W'], 'E' : [[1, 0], 'N', 'S']}
        
        for ch in instructions:
            if ch == 'G':
                v = d[direction][0]
                vector[0] += v[0]
                vector[1] += v[1]
            elif ch == 'R':
                direction = d[direction][2]
            else:
                direction = d[direction][1]
                
        if direction != 'N' or vector == [0, 0]:
            return True
        return False