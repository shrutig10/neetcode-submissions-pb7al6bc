class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # need to find max of first window by iterating through
        # monotonic stack or we can use a max heap
        # keep the index in with the value
        # add elements to the heap with their index
        # if the top is in the window, then add to the max list
        # pop the heap until the top is in the window
        # as we keep interating through the list, keep adding elements to the heap

        res = []
        maxHeap = []

        for i in range(k - 1):
            heapq.heappush(maxHeap, (-nums[i], i))

        for i in range(k - 1, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            while maxHeap[0][1] < (i - k + 1):
                heapq.heappop(maxHeap)
            res.append(-maxHeap[0][0])

        return res


        