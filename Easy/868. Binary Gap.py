class Solution:
    def binaryGap(self, N: int) -> int:
        
        binary = bin(N).replace("0b", "")
        count = 0
        distance = 0
        for ch in binary:
            if ch == '1':
                if distance < count:
                    distance = count
                count = 1
            else:
                count += 1
        return distance
       
    