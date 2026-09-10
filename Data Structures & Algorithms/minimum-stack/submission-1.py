class MinStack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if self.stack is None:
            return None
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        
