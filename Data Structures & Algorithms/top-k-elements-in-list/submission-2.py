class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a max heap --> store tuples (frequency, value of the number)
        # iterate through array; creating a map that stores frequencies
        # pop the heap k times to get the k most frequent elements
        # O(nlogn), O(n) --> number of elements
        # O(n) 
        # create an array --> bucket
        # iterate through array and create map
        # go through the map, store the key (number) in the correct bucket
        # iterate backwards through the buckets, append k elements

        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in frequencies.keys():
            buckets[frequencies[num]].append(num)

        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        