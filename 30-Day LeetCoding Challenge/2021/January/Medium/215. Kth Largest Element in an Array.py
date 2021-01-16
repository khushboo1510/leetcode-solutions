# https://leetcode.com/problems/kth-largest-element-in-an-array/
    
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
     
        pivot = nums[0]
        left, equal, right = [], [], []
        ln = en = rn = 0
        for num in nums:
            if num < pivot:
                left.append(num)
                ln += 1
            elif num == pivot:
                equal.append(num)
                en += 1
            else:
                right.append(num)
                rn += 1
                
        if k <= rn:
            return self.findKthLargest(right, k)
        elif k - rn <= en:
            return equal[0]
        else:
            return self.findKthLargest(left, k - en - rn)
