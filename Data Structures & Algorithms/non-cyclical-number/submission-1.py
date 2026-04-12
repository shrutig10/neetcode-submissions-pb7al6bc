class Solution:
    def isHappy(self, n: int) -> bool:
        # use a set to store numbers that we've seen before
        # get the last digit by doing num % 10
        # square that number, add it to a sum
        # integer division by 10 to get the next number
        # while num is not 0
        # if the sum is 1, return true
        # if the sum is somethign we;ve seen before, return false
        # otherwise keep going

        seen = set()
        curSum = 0

        while curSum not in seen:
            seen.add(curSum)
            curSum = 0
            while n != 0:
                curSum += (n % 10) * (n % 10)
                n //= 10

            if curSum == 1:
                return True
            n = curSum
        
        return False

        