"""
942. DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
"""

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        N = len(S)
        I = 0
        D = N
        output = []
        last_ch = ""
        for ch in S:
            if ch == 'I':
                output.append(I)
                I += 1
                last_ch = 'I'
            else:
                output.append(D)
                D -= 1
                last_ch = 'D'
                
        if 'D' in last_ch:
            output.append(D)
        else:
            output.append(I)
        return output
                