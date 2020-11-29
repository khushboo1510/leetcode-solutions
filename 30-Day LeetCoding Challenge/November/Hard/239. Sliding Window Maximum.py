# https://leetcode.com/problems/sliding-window-maximum/
    
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, result = [], []
        for i in range(k-1):
            heapq.heappush(heap,(-nums[i],i))
        
        for i in range(k - 1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while i - k >= heap[0][1]:
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result
