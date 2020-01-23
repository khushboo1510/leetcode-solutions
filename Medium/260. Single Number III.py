class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        counter = collections.Counter(nums)
        lst = []
        for key, value in counter.items():
            if value == 1:
                lst.append(key)
        return lst
