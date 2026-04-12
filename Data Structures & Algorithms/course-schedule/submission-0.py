class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # bfs 
        # create a array where the index is the course and the value is the prerequisite it requires
        # perform a topological sort using kahn's algorithm
        # use a queue and put all vertices (Courses) with in degree 0 (no prerequisites) and process their neighbors
        # while processing neighbors, reduce in degree by 1, if in degree becomes 0, then add to queue
        # if queue is empty return true (all classes have been processed) otherwise return false

        if not prerequisites:
            return True

        indegree = [0] * numCourses
        forward_map = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            indegree[prereq[0]] += 1
            forward_map[prereq[1]].append(prereq[0])

        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i) 

        while queue:
            cur_course = queue.popleft()
            for eligible_class in forward_map[cur_course]:
                indegree[eligible_class] -= 1
                if indegree[eligible_class] == 0:
                    queue.append(eligible_class)
        
        for course in indegree:
            if course != 0:
                return False

        return True
        


        