class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If we don't have any digits, we
        # can't do any mapping
        if not digits:
            return []

        # Creating a mapping for each digit
        # and their letters
        digitMapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Storing our current and final information
        curPath, result = [], []

        # Creating our recursive function
        def DFS(index):
            # Save the current combination as we have
            # found a valid combination
            if index == len(digits):
                result.append("".join(curPath))
                return

            # Getting our corresponding list of letters
            letters = digitMapping[digits[index]]

            # Traverse through each character in 
            # the letters we extracted
            for character in letters:
                # Do the usual backtracking
                curPath.append(character)
                DFS(index + 1)
                curPath.pop()

        # Begin our recursive journey
        DFS(0)
    
        # Return our final result
        return result