class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [item for item, count in collections.Counter(nums).items() if count > 1]
