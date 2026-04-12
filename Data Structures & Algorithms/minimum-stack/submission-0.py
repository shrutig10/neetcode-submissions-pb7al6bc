class MinStack:

    def __init__(self):
        self.stack = []
        self.orderedStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.orderedStack: 
            val = min(val, self.orderedStack[-1])
        self.orderedStack.append(val) # doing this makes it so that you don't have to check identity during pop

    def pop(self) -> None:
        self.orderedStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.orderedStack[-1]
        
