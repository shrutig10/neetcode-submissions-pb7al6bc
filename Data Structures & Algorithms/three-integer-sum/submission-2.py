class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solve 2sum by using a hashmap
        # sort the array
        # we can fix the first number and then find the other two numbers
        # don't want to use a hashmap, so we can instead use a left and right pointer
        # start the left after the current number, right at the end
        # add the left, right, and current number 
        # if you get 0, then add it to the list
        # increment left until you hit a new number and decrement right until you hit a new number
        # if you can't make 0, then increment left if you were too less
        # decrement right if you were too much

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                test = nums[i] + nums[l] + nums[r]
                if test == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif test < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1 

        return res


