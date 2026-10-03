import string

class Solution:
    # This is a helper function that gets all the
    # valid transformations for a particular word
    # (it's valid by one character)
    def getValidTransformations(self, word: str, wordSet: set) -> List[str]:
        # First convert to a mutable structure
        charList = list(word)

        # Store all valid neighbors
        neighbors = []

        # Traverse through each character
        for character in range(len(charList)):
            # Saving the original character
            original = charList[character]

            for letter in string.ascii_lowercase:
                # Skip if it's the original character
                if letter == original:
                    continue

                # Switch the character to a new candidate
                charList[character] = letter
                candidate = "".join(charList)

                # Collect the word if it's a neighbor
                if candidate in wordSet:
                    neighbors.append(candidate)

            # Revert the character back to its original
            charList[character] = original
                
        # Return all neighbors we collected
        return neighbors


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the end word is unreached, simply
        # return 0
        if endWord not in wordList:
            return 0

        # Create a set for fast lookup
        wordSet = set(wordList)

        # Create our queue
        queue = deque()

        # Append the first word with a distance
        # of 1 as it is the beginning word
        queue.append((beginWord, 1))

        # Create our visited set
        visited = set()
        visited.add(beginWord)

        # Perform BFS
        while queue:
            # Extract the next word and its distance
            nextWord, nextDist = queue.popleft()

            # Collect all neighbors from the next word
            neighbors = self.getValidTransformations(nextWord, wordSet)

            # Traverse each neighbor
            for neighbor in neighbors:
                # Skip if we already visited this neighbor
                if neighbor in visited:
                    continue

                # If it is the end word, we found a path
                if neighbor == endWord:
                    return nextDist + 1

                # Add the word to our queue
                queue.append((neighbor, nextDist + 1))

                # Mark it as visited
                visited.add(neighbor)

        # If our BFS algorithm fully runs and
        # doesn't find anything, it means it was
        # unreachable, so return 0
        return 0