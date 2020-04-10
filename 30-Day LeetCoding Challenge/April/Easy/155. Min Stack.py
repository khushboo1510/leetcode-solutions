"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.minList = []
        

    def push(self, x: int) -> None:
        self.l.append(x)
        if not self.minList or x <= self.minList[-1]:
            self.minList.append(x)

    def pop(self) -> None:
        x = self.l.pop()
        if self.minList and x == self.minList[-1]:
            self.minList.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.minList[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()