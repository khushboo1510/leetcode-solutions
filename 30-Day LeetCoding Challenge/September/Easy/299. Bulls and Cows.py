# https://leetcode.com/problems/bulls-and-cows/
    
# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

# Please note that both secret number and friend's guess may contain duplicate digits.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        d1, d2 = defaultdict(int), defaultdict(int)
        bull, cows = 0, 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                continue
            d1[secret[i]] += 1
            d2[guess[i]] += 1
            
        for key, value in d1.items():
            if key in d2:
                cows += min(value, d2[key])
        
        return f'{bull}A{cows}B'