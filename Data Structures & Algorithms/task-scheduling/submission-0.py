class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Use a counter to count frequencies of
        # all numbers
        taskFreqs = Counter(tasks)

        # Get our maximum frequency
        maxFreq = max(taskFreqs.values())

        # Calculate our k (number of distinct tasks
        # sharing the same max frequency)
        k = sum(1 if freq == maxFreq else 0 for freq in taskFreqs.values())

        # Return the minimum CPU cylces needed
        return max(len(tasks), (maxFreq - 1) * (n + 1) + k)
