class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])        
        luckynum = []
        
        for i in range(m):
            col_index = matrix[i].index(min(matrix[i]))
            max_num = matrix[i][col_index]
            
            for j in range(m):
                if max_num < matrix[j][col_index]:
                    max_num = matrix[j][col_index]
                    
            if(max_num == matrix[i][col_index]):
                luckynum.append(max_num)
        
        return luckynum