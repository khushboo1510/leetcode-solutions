class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(0, len(nums)):
            n = target - nums[i]
            if d.get(n) != None and d.get(n) != i:
                return [i, d.get(n)]
            d[nums[i]] = i