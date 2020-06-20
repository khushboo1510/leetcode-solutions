# https://leetcode.com/problems/longest-duplicate-substring/
    
# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

# Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        self.n = len(S)
        left = 0
        right = self.n
        mLen, mString = 0, ""
        self.prime = 2 ** 63 - 1
                    
        def rabin_carp(k):
            power_last = pow(26, k, self.prime)
            rolling_hash = 0
            seen = set()
            for i in range(0,k):
                rolling_hash = (rolling_hash * 26 + ord(S[i])) % self.prime
            seen.add(rolling_hash) 
            
            i = 0
            while(k < self.n):
                rolling_hash = (rolling_hash * 26 + ord(S[k]) - power_last*ord(S[i])) % self.prime
                if rolling_hash in seen:
                    return S[i+1:k+1]
                else:
                    seen.add(rolling_hash)
                k += 1
                i += 1
            return ""
            
        while left < right:
            mid = (right + left)//2
            ans = rabin_carp(mid)
            l = len(ans)
            if l > 0:
                if l > mLen:
                    mLen, mString = l, ans
                left = mid + 1
            else:
                right = mid
                
        return mString