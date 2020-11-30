# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if not s:
            return 0
        
        d = defaultdict(int)
        
        for ch in s:
            d[ch] += 1
            
        invalids, n = [], len(s)
        for key, value in d.items():
            if value < k:
                invalids.append(key)
        if not invalids:
            return n
        maximum = 0        
        for interval in re.sub('|'.join(invalids), ' ', s).split(' '):
            maximum = max(maximum, self.longestSubstring(interval, k))
        return maximum
