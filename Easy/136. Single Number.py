class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_lst = collections.Counter(nums)
        for num in nums:
            if count_lst[num] == 1:
                return num
