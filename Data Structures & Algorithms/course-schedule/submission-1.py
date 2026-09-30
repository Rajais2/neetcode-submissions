class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Creating our graph
        graph = defaultdict(list)

        # Building our graph (adjacency list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Preparing to store information garnered
        # by our DFS
        currently_explored = set()
        visited = set()

        # Creating our DFS recursive function
        def DFS(course):
            # Found a cycle so return False
            if course in currently_explored:
                return False

            # The node has been processed already
            if course in visited:
                return True

            # Add the node since it's being explored
            currently_explored.add(course)

            # DFS on all connected neighbors
            for neighbor in graph[course]:
                # Return false if any neighbor makes a cycle
                if not DFS(neighbor):
                    return False

            # It didn't cause a cycle so update
            # its state accordingly
            currently_explored.discard(course)
            visited.add(course)
            return True

        # Go up to numCourses 
        for course in range(numCourses):
            # Skip the node if we have visited it already
            if course in visited:
                continue

            # Otherwise, run our DFS algorithm on the course
            if not DFS(course):
                return False

        return True