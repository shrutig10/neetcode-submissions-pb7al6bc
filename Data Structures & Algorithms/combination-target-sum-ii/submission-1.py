class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        # can only select a candidate once per entry in output
        # decision: include the number or not
        # cur sum --> does adding this number make us exceed the target? if so, don't add and recur
        # otherwise add and recur with it
        # base case: does the cur sum = target? if so add this to our res
        # base case: index is out of bounds? return <- stop exploring

        res = set()
        candidates.sort()

        def backtrack(idx, cur_sum, subset):
            if cur_sum == target:
                res.add(tuple(subset))
                return
            if idx == len(candidates) or cur_sum > target:
                return

            subset.append(candidates[idx])
            backtrack(idx + 1, cur_sum + candidates[idx], subset)

            subset.pop()
            backtrack(idx + 1, cur_sum, subset)

        backtrack(0, 0, [])
        return [list(i) for i in res]
            