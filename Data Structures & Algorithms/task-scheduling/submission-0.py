class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # what type of task do we have to do the most amount of times?
        # this is what we prefer to do first
        # can use a max heap to store this information
        # pop item when we complete task, if still tasks left for that identity, wait n times before adding back to the heap
        # when to add back to the heap? store in a list? where index corresponds to how many cycles are left? and you can adjust per iteration and add back to heap the element at index 0 --> lots of runtime
        # use a queue --> when we add an element to the queue, add along its next available time
        # if the heap is empty change total time to time in queue and push that back onto the heap
        # every iteration check if the time matches element in the heap, and then push back onto heap

        time = 0
        freq = defaultdict(int)
        heap = []
        for task in tasks:
            freq[task] += 1
        
        for task, amt in freq.items():
            heapq.heappush(heap, -amt)
        
        cooldown = []
        while heap:
            cur_task = heapq.heappop(heap)
            cur_task += 1  # amt is negative due to max heap, so add 1
            time += 1
            if cur_task:
                cooldown.append((cur_task, time + n))
            if cooldown and time == cooldown[0][1]:
                heapq.heappush(heap, cooldown[0][0])
                cooldown.pop(0)
            if not heap and cooldown:
                time = cooldown[0][1]
                heapq.heappush(heap, cooldown[0][0])
                cooldown.pop(0)

        return time


