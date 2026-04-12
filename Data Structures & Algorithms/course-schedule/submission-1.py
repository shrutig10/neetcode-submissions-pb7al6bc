from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # graph where a prereq is pointing to a class it unlocks
        # classes you can take will have 0 items pointing to it (inDegree is 0)
        # create a class adjacency list: class | [prereqs] --> array
        # another prereq adjacency list: prereq | [class this unlocks] --> array
        # go through class adjacency list and add classes with no prereqs to a queue
        # remove that class from other classes using the prereq adjacency list
        # keep a count of how many classes have been finished 
        # once the queue finishes, if count = numcourses, then true, else false

        classes = [0] * numCourses
        unlock = [[] for _ in range(numCourses)]

        for entry in prerequisites:
            course = entry[0]
            prereq = entry[1]

            classes[course] += 1
            unlock[prereq].append(course)

        q = deque()

        for i in range(len(classes)):
            if not classes[i]:
                q.append(i)

        taken = 0

        while q:
            course = q.popleft()
            taken += 1
            for future_class in unlock[course]:
                classes[future_class] -= 1
                if classes[future_class] == 0:
                    q.append(future_class)

        return taken == numCourses
        