class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # implement a bucket sort
        # # of buckets = # of elements
        # array would be 1-indexed --> add one extra element to the bucket
        # count the frequency, every time frequency of an element increases, move the number to the next bucket
        # go from the greatest bucket down and pick the first k elements that appear

        count = {}
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            buckets[freq].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        


