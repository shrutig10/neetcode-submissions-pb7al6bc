class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       # keep track of negative numbers?
       # keep a running maximum and current, both of these set to first number or 1
       # at every number, we will multiply with our current num
       # if the current number is 0, then we can reset our current to 1
       # current running minimum --> most negative number
       # if the number is negative, this negative number will become a large positive number
       # if it hits 0, also reset to 1
       # what if the current number is larger than the product of it and the other numbers

        maximum = curMax = curMin = nums[0]

        for i in range(1, len(nums)):
            prod = nums[i] * curMax
            curMax = max(nums[i], prod, nums[i] * curMin)
            curMin = min(nums[i], prod, nums[i] * curMin)

            maximum = max(maximum, curMax)

        return maximum


    # [1, 2, -3, 4]
    # max = 4
    # curMax = 4
    # curMin = -6

    # 1, 2, 0, -3
    # max = 2
    # curMax = 0
    # curMin = -3


