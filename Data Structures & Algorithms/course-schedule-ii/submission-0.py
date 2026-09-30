class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create the graph
        graph = defaultdict(list)
                
        # Make an indegree array
        indegree = [0] * numCourses

        # Will hold the final answer
        order = []

        # Build the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)

            # Increment the indegrees as accordingly
            indegree[course] += 1

        # Make a queue with values with zero indegree
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)

        # BEGIN PROCESSING COURSES!!!!!!!!!!!!!!!
        while queue:
            # Get the next course
            course = queue.popleft()

            # Add it our processing order
            order.append(course)

            # Go through neighbors and decrease their indegree
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                
                # Add the node if no more nodes are connected
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Return either something or nothing
        if len(order) == numCourses:
            return order
        else:
            return []
