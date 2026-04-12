class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # push temperature and index onto stack
        # while the current temperature you are looking at is 
        # larger than the top of the stack:
        # pop the top of the stack and set it's index in result
        # to the difference between the current temp's index and 
        # the top of the stack's index (the popped element)

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)

        return res