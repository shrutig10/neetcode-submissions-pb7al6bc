class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # one solution = sort array -> check for consecutive sequence, does not run O(n) time
        # use a hashmap; key --> number, value --> length of the longest consecutive sequence ending at that number
        # loop through array, if the previous number exists, add this number with value being 1 more than the value of the previous
        # if number already exists in the hash map then don't add it again
        # return max value from the hash map

        if len(nums) == 0:
            return 0
        
        sequences = {}

        for num in nums:
            sequences[num] = sequences.get(num - 1, 0) + 1
            i = num + 1
            while i in sequences:
                sequences[i] = sequences[i - 1] + 1
                i += 1

        return max(sequences.values())
        