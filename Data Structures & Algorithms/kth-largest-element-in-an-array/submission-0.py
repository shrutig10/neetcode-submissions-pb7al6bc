class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # can use a max-heap to store the numbers --> multiply by -1
        # pop k elements at the end; kth element that we pop is the kth largest element
        # initialize empty heap
        # iterate throught the array, add values to the heap
        # pop k times, taking the last element

        heap = []

        for num in nums:
            heapq.heappush(heap, num * -1)

        for i in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap) * -1