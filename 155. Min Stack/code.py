class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min.append(val)
        else:
            self.stack.append(val)
            if self.top() >= self.min[-1]:
                self.min.append(self.min[-1])
            else:
                self.min.append(self.top())

    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
       
    def getMin(self) -> int:
        return self.min[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()