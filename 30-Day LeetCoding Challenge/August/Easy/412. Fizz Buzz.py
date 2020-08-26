# https://leetcode.com/problems/fizz-buzz/
    
# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = 'Fizz'
        buzz = 'Buzz'
        result = []
        
        for i in range(1, n + 1):
            word = ''
            if i % 3 == 0:
                word += fizz
            if i % 5 == 0:
                word += buzz
            if not word:
                word = str(i)
            result.append(word)
            
        return result