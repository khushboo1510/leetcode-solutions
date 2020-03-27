class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        if n == 0:
            return ""
        dp = [[False for x in range(n)]
                    for y in range(n)]
        
        dp[0][0] = True
        count = 1
        maxLength = 0
        start,end = 0,0
        
        for i in range(1,n):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i - j < 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    count += 1
                    if i - j > maxLength:
                        maxLength = i - j
                        start = j
                        end = i
        return s[start:end+1]