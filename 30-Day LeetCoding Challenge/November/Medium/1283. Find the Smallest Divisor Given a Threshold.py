# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
    
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# It is guaranteed that there will be an answer.

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 0, max(nums) + 1
        
        while start + 1 < end:
            mid = (start + end)//2
            if sum(ceil(num/mid) for num in nums) <= threshold:
                end = mid
            else:
                start = mid        
        return end
