# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        a = dict()
        for i, num in enumerate(arr):
            a[num] = i
            
        for piece in pieces:
            if piece[0] not in a:
                return False
            n = len(piece)
            if arr[a[piece[0]]:a[piece[0]]+n] != piece:
                return False
            
        return True
