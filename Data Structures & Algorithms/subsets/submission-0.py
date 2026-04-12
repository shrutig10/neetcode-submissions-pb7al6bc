class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursive backtracking
        # two options: include this element or not
        # start with empty array
        # two recursive paths: add this element or don't
        # once you reach the end of the list, append you subset to the result

        res = []

        def getSubsets(cur_subset, idx):
            if idx >= len(nums):
                res.append([int(x) for x in cur_subset.split(' ')[:-1]])
                return
            getSubsets(cur_subset, idx + 1)
            getSubsets(cur_subset + str(nums[idx]) + ' ', idx + 1)

        getSubsets("", 0)
        return res

        