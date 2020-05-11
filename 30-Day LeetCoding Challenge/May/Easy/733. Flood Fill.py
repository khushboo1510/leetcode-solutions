"""
https://leetcode.com/problems/flood-fill/

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        queue = [[sr, sc]]
        currColor = image[sr][sc]
        rows, cols = len(image), len(image[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        while queue:
            i, j = queue.pop(0)
           
            if not visited[i][j]:
                visited[i][j] = True
                
                if image[i][j] == currColor:
                    image[i][j] = newColor
                    for dr,dc in directions:
                        if i+dr < 0 or i+dr == rows or j+dc == cols or j+dc < 0:
                            continue
                        queue.append([i + dr, j + dc])
        
        return image