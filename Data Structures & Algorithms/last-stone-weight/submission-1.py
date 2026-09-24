class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # keep a max heap of all the stones
        # pop the two elements from the heap
        # do smash logic
        # push the stone on if x < y
        # while len of the heap > 1

        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            leftover = y - x 
            if leftover:
                heapq.heappush(heap, leftover)
        
        return -heap[0] if heap else 0

        