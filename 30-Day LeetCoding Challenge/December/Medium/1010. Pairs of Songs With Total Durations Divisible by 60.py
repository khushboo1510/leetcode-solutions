# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
    
# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        self.factorials = {1:1, 0:1}
        d = defaultdict(int)
        for song in time:
            d[song % 60] += 1
        count = 0
        songs = list(d.keys())

        def fact(n):
            if n not in self.factorials:
                self.factorials[n] = n * fact(n - 1)
            return self.factorials[n]
        
        for i, song1 in enumerate(songs):
            if d[song1] > 1 and (song1*2) % 60 == 0:
                count += (fact(d[song1]) // (self.factorials[d[song1] - 2] * 2))
            
            for j, song2 in enumerate(songs[i+1:], i + 1):
                if (song1 + song2) % 60 == 0:
                    count += d[song1] * d[song2]
        
        return count
