class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []

        i = 0 
        while i < len(sortedNums):
            while i != 0 and i < len(sortedNums) - 1 and sortedNums[i] == sortedNums[i - 1]:
                i += 1

            a = sortedNums[i]
            l, r = i + 1, len(sortedNums) - 1

            while l < r:
                sum = a + sortedNums[l] + sortedNums[r]
                if sum == 0:
                    arr = [a, sortedNums[l], sortedNums[r]]
                    if arr not in res:
                        res.append(arr)
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1

            i += 1

        return res

        