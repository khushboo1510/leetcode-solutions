"""
https://leetcode.com/problems/friend-circles/

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Note:
    1. N is in range [1,200].
    2. M[i][i] = 1 for all students.
    3. If M[i][j] = 1, then M[j][i] = 1.
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        n = len(M)
        seen = [0] * n
        count = 0
        
        for i in range(n):
            if seen[i] == 1:
                continue
                
            queue = [i]
            while queue:
                x = queue.pop(0)
                seen[x] = 1

                for j in range(1, n):
                    if M[x][j] == 1 and seen[j] != 1:
                        queue.append(j)
                        
            count += 1
        
        return count