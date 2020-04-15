"""
Given an array of strings, group anagrams together.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = 1
        d = {}
        anagrams = []
        
        for word in strs:
            
            x = ''.join(sorted(word))
            
            if not d.get(x):
                new = []
                d[x] = count
                count += 1
                new.append(word)
                anagrams.append(new)
            else:
                i = d.get(x)
                anagrams[i-1].append(word)
                
        return anagrams
            