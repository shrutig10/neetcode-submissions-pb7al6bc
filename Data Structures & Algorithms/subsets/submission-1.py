class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # explore all possible combinations
        # decision: take the number or to skip the number
        # base case: if we've reached the end of the array, then subset to result

        res = []

        def backtrack(idx, cur):
            if idx == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[idx])
            backtrack(idx + 1, cur)
            
            cur.pop()
            backtrack(idx + 1, cur)


        backtrack(0, [])
        return res

        