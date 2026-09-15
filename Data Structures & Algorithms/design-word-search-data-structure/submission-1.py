class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.isEnd = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        currentNode = self.root

        for char in word:
            # Create the child if it doesn't exist
            if char not in currentNode.children:
                currentNode.children[char] = self.Node()

            currentNode = currentNode.children[char]

        # Mark the end of the word
        currentNode.isEnd = True

    def search(self, word: str) -> bool:

        def DFS(curNode, index):
            # Reached the end of the word
            if index == len(word):
                return curNode.isEnd

            char = word[index]

            # Normal character
            if char != '.':
                if char not in curNode.children:
                    return False

                return DFS(curNode.children[char], index + 1)

            # Wildcard: try every possible child
            for child in curNode.children.values():
                if DFS(child, index + 1):
                    return True

            return False

        return DFS(self.root, 0)
