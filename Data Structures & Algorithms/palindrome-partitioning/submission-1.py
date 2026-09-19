class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Setting up to store current and
        # final information
        curPath, result = [], []

        # Creating our recursive function
        def DFS(start):
            # We have a found a valid palindrome
            if start == len(s):
                result.append(curPath.copy())
                return

            # Traversing the string from start and onwards
            for end in range(start, len(s)):
                candidateSubStr = s[start:end + 1]

                # Checking if it's a palindrome and explore
                # if it is
                if candidateSubStr == candidateSubStr[::-1]:
                    curPath.append(candidateSubStr)
                    DFS(end + 1)
                    curPath.pop()

        # Begin our recursive journey
        DFS(0)

        # Return our final result
        return result