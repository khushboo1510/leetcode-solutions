# https://leetcode.com/problems/buddy-strings/
    
# Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n = len(A)
        if n != len(B):
            return False
        
        if A == B and len(set(B)) < n:
            return True
        
        count, diffs = 0, []
        for i in range(n):
            if A[i] != B[i]:
                count += 1
                if count > 2:
                    return False
                diffs.append(i)

        if count == 2:
            i, j = diffs
            if A[i] == B[j] and B[i] == A[j]:
                return True
        return False
