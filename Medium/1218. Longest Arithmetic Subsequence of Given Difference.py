class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        #Solved using dynamic programming

        dp = {}

        #initializing each element with 1
        #As the longest arithmetic subsequence of any single element is 1
        for num in arr:
            dp[num] = 1

        #set of previously visited elements
        seen = set()

        for i in range(1, len(arr)):
            seen.add(arr[i-1])
            if(arr[i] - difference in seen):
                dp[arr[i]] = 1 + dp[arr[i] - difference]

        return max(dp.values())
    