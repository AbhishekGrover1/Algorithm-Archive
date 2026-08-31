from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list and calculate in-degrees
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Queue all courses that have no prerequisites (in-degree == 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        # Kahn's Algorithm (BFS)
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If order contains all courses, return it; otherwise, a cycle exists
        return order if len(order) == numCourses else []