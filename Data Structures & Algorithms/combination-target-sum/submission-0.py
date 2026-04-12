class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking - try all combinations
        # if we've reached the end of the list: return
        # is the sum equal to target -> add the numbers to our result, return
        # decision: add this number or skip
        # add the number
        # if less or equal then recurse 
        # is sum greater than target -> skip first recursion
        # remove the last added number and then try again, but with the next index

        res = []

        def backtrack(idx, cur_sum, subset):
            if idx == len(nums):
                return
            if cur_sum == target:
                res.append(subset.copy())
                return
            
            cur_sum += nums[idx]
            subset.append(nums[idx])

            if cur_sum <= target:
                backtrack(idx, cur_sum, subset)
            
            cur_sum -= nums[idx]
            subset.pop()

            backtrack(idx + 1, cur_sum, subset)

        backtrack(0, 0, [])
        return res
