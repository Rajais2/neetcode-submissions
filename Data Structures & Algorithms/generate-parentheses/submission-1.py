class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Creating a resulting final list to store
        # all the answers
        result = []

        curString = []

        # Creating our recursive backtracking function
        def DFS(open_count, close_count):
            # We found a well-formed parentheses string
            if open_count == n and close_count == n:
                result.append("".join(curString))
                return
            
            # Checking if we can add an opening paranthesis
            if open_count < n:
                curString.append('(')
                DFS(open_count + 1, close_count)
                curString.pop()

            # Checking if we can add a closing paranthesis
            if close_count < open_count:
                curString.append(')')
                DFS(open_count, close_count + 1)
                curString.pop()

        # Calling our recursive function
        DFS(0, 0)

        # Returning our final answer
        return result
