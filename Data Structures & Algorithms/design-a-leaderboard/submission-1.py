class Leaderboard:

    def __init__(self):
        # hashmap (key: playerId, value: score)
        # heap --> store tuples with (score, playerID) <- pop the top k and save
        # reinsert them into my heap
        # extra check that they still exist in the heap? and that the score is what we expect?
        # use the hashmap to remove from the heap heapq.remove(heap, (score, playerid))

        self.mapping = {}
        self.heap = []
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.mapping:
            self.mapping[playerId] = 0
        else:
            self.heap.remove((self.mapping[playerId], playerId))
            heapq.heapify(self.heap)
        
        self.mapping[playerId] -= score
        heapq.heappush(self.heap, (self.mapping[playerId], playerId))
        

    def top(self, K: int) -> int:
        total = 0
        popped = []

        for i in range(K):
            popped.append(heapq.heappop(self.heap))
            total += popped[-1][0] * -1
        
        while popped:
            heapq.heappush(self.heap, popped.pop())

        return total
        

    def reset(self, playerId: int) -> None:
        self.heap.remove((self.mapping[playerId], playerId))
        heapq.heapify(self.heap)
        del self.mapping[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
