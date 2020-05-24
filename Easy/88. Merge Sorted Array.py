"""
https://leetcode.com/problems/merge-sorted-array/submissions/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

1. The number of elements initialized in nums1 and nums2 are m and n respectively.
2. You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n <= 0:
            return
        i = j = 0
        arr = []
        while i < len(nums1):
            if i < m:
                arr.append(nums1[i])
                if j >= n or arr[0] < nums2[j]:
                    nums1[i] = arr.pop(0)
                else:
                    nums1[i] = nums2[j]
                    j += 1
            else:
                if arr and (j >= n or arr[0] < nums2[j]):
                    nums1[i] = arr.pop(0)
                else:
                    nums1[i] = nums2[j]
                    j += 1
            i += 1