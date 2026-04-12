class MinStack:

    def __init__(self):
        # implement our stack by using an array
        # push will append to the array
        # pop will pop from the array
        # top will get the last element in the array
        # have a second stack called min
        # if the element that is pushed is less than the top of min, push new element onto min
        # if element popped is min, pop from min stack as well

        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.getMin():
            self.minStack.append(val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        if self.getMin() == val:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
