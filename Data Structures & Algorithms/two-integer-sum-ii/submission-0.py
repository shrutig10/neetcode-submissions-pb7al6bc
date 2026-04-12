class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while end > start:
            res = numbers[start] + numbers[end]
            if res == target:
                return [start + 1, end + 1]
            if res < target:
                start += 1
            else:
                end -= 1