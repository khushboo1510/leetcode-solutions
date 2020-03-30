class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        sList = s.split(" ")
        maxLen =  len(max(sList, key=len))
        
        ans = []
        for x in range(maxLen):
            str = ""
            for word in sList:
                if len(word) < x + 1:
                    str += " "
                else:
                    str += word[x]
            ans.append(str.rstrip(" "))
        
        return ans