class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a min heap
        # store entries in the heap as a tuple --> (dist, [x,y])
        # steps
        # initialize my min heap
        # iterate through points, calculating the euclidean distance
        # insert it into the heap
        # take the top k elements from the heap and store in a list
        # return that list

        heap = []

        for point in points:
            dist = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            heapq.heappush(heap, (dist, [point[0], point[1]]))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res