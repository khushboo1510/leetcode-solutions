class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        
        dp = [[False for x in range(n)]
                     for y in range(n)]
        
        dp[0][0] = True
        count = 1
        
        for i in range(1,n):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i - j < 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    count += 1
        
        return count