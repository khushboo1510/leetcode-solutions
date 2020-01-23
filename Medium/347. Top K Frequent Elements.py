class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = dict(collections.Counter(nums).items())
        return heapq.nlargest(k, dict1, key=dict1.get)
