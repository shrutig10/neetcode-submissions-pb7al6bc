class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # decision: add this element or skip it
        # base case: if we reach the end of the array
        # we can add the subset as a tuple in a set
        # at the end, convert each tuple to a list

        nums.sort() # nlogn
        res = set()

        def backtrack(subset, idx):
            if idx == len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[idx])
            backtrack(subset, idx + 1)

            subset.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(subset, idx + 1)

        backtrack([], 0)
        return [list(i) for i in res]