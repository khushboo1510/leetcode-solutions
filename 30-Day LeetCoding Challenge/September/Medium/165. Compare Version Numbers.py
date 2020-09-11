# https://leetcode.com/problems/compare-version-numbers/
    
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise, return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.

# The . character does not represent a decimal point and is used to separate number sequences.

# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = list(map(int, version1.split('.')))
        l2 = list(map(int, version2.split('.')))
        
        while l1 or l2:
            if l1 and l2:
                if l1[0] < l2[0]:
                    return -1
                elif l1[0] > l2[0]:
                    return 1
                else:
                    l1.pop(0)
                    l2.pop(0)
            elif l1:
                if l1[0] != 0:
                    return 1
                else:
                    l1.pop(0)
            elif l2[0] != 0:
                return -1
            else:
                l2.pop(0)
                
        return 0
                