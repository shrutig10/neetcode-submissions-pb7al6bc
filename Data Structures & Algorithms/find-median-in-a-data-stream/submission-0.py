class MedianFinder:

    def __init__(self):
        # stored the current median always? can't do this because doesn't work in odd cases
        # need to store the numbers from the stream
        # 2 heaps: one min and one max
        # min heap stores the second half of the stream
        # max heap stores the first of the stream

        self.minHeap = []
        self.maxHeap = []

        

    def addNum(self, num: int) -> None:
        # if element is smaller than min heap, push onto max heap
        # else push onto min heap
        # if heaps becomes very imbalanced (difference is >= 2), push from longer heap to shorter heap
        # when we rebalance, you multiply by negative one!!! 

        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
        else:
            if num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)

        while abs(len(self.minHeap) - len(self.maxHeap)) >= 2:
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))


        

    def findMedian(self) -> float:
        # if odd, take from the larger sized heap, else take mean of min and max heaps' tops

        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]
        
        