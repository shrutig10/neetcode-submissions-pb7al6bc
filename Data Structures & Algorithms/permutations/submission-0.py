class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       # there exists n! permutations where n is the number of elements
       # backtracking
       # base case: when length of permutation is length of array
       # decision: add this element or skip it
       # go through array, add element and keep recursing
       # take out the element and keep recursing <- set to false in boolean array

        res = []

        def backtrack(perm, chosen):
            if len(perm) == len(nums):
                res.append(perm[:])
        
            for i in range(len(nums)):
                if not chosen[i]:
                    perm.append(nums[i])
                    chosen[i] = True
                    backtrack(perm, chosen)
                    perm.pop()
                    chosen[i] = False

        backtrack([], [False] * len(nums))
        return res

        