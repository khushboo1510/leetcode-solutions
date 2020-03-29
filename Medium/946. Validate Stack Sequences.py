class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        flag = True
        
        for num in pushed:
            stack.append(num)
            while stack:
                if stack[-1] != popped[0]:
                    flag = False
                    break
                flag = True
                stack.pop()
                popped.pop(0)
            
        return flag