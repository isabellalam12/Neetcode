class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            prev_min = self.stack[-1][1]
        else: 
            prev_min = 2**31 - 1
        mini = min (prev_min, val)
        self.stack.append((val, mini))

        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
