class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # need to use a heap for this
        # need to use a min heap
        # size of the heap = k
        # top of the heap = kth largest
        # bottom of the heap = max element

        self.heap = []
        self.k = k

        for num in nums:
            heapq.heappush(self.heap, num)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        # if pushing this element causes size > k, pop the  heap and then return top
        heapq.heappush(self.heap, val)
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
