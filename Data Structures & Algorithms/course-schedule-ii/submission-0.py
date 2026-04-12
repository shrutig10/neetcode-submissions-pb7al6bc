class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # keep track of which courses require how many prerequisites <-- number of indegrees
        # keep track of which courses open up other courses
        # bfs
        # start with courses that require no prereqs (indegree = 0)
        # go through their neighbors (from the opening up list) and reduce their indegree by 1
        # any class that has 0 for their indegree will be added to the queue
        # if all courses have been added to result, return that else return []

        indegree = [0] * numCourses
        prereqs = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            prereqs[b].append(a)
        
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        res = []

        while queue:
            cur_course = queue.popleft()
            res.append(cur_course)
            for nei in prereqs[cur_course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(res) == numCourses:
            return res
        else:
            return []

        