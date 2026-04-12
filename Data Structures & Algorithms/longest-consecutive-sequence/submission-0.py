class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        numsInDict = {}
        longest = 0

        for num in sortedNums:
            if num in numsInDict:
                continue

            curAmount = 1
            if num - 1 in numsInDict:
                curAmount += numsInDict[num - 1]

            numsInDict[num] = curAmount
            longest = max(longest, curAmount)

        return longest
            