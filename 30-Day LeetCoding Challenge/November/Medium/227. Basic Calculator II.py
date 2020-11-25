# https://leetcode.com/problems/basic-calculator-ii/
    
# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.    

class Solution:
    def calculate(self, s: str) -> int:
        stack, opr, num = [], '+', ''
        for ch in s+'#':
            if ch == ' ':
                continue
            if ch.isdigit():
                num += ch
            else:
                if opr == '-':
                    stack.append(-int(num))
                elif opr == '*':
                    stack.append(stack.pop() * int(num))
                elif opr == '/':
                    stack.append(int(stack.pop() / int(num)))
                else:
                    stack.append(int(num))
                opr = ch
                num = ''
        return sum(stack)
