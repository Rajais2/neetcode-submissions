# An individual Trie Node
class TrieNode:
    def __init__(self) -> None:
        # Children, is a word, and the word itself
        self.children = {}
        self.isWord = False
        self.word = None

# Represents a Trie  
class PrefixTree:
    def __init__(self):
        # Here, we need to create a root
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Set up a current pointer to traverse the tree
        current = self.root

        # Traverse through all characters in our word
        for character in word:
            # Checking if we have the character already, so
            # we move our current pointer to that character
            if character in current.children:
                current = current.children[character]
            else:
                # Make a new Trie Node and attach it to our
                # current pointer
                new_node = TrieNode()
                current.children[character] = new_node
                current = current.children[character]

        # Making this node as a valid word
        # and the word itself
        current.isWord = True
        current.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # First, create a trie
        trie = PrefixTree()

        # Insert our words into our new Trie
        for word in words:
            trie.insert(word)

        # Contains the final results
        result = []

        # Creating all possible directions
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        # Creating our recursive backtracking function
        def DFS(row, col, node):
            # If the character we're on is not
            # a child, we stop this path
            if board[row][col] not in node.children:
                return

            # Move into that Trie node
            node = node.children[board[row][col]]

            # If it is a completed word, then we
            # add it to our final list as we have found it
            if node.isWord:
                result.append(node.word)
                node.isWord = False

            # Mark the current cell as visited
            original = board[row][col]
            board[row][col] = "#"

            # Traverse in all four possible directions
            for dr, dc in directions:
                # Getting the new positions
                new_row = row + dr
                new_col = col + dc

                # Skip if we are out of bounds or the cell
                # is visited already
                if (new_row < 0 or new_row >= len(board)
                        or new_col < 0 or new_col >= len(board[0])
                        or board[new_row][new_col] == "#"):
                            continue
                
                # Explore the new paths
                DFS(new_row, new_col, node)

            # Restore the cell to its original state
            board[row][col] = original
            

        # Begin our recursive journey!!!!!!!!!!!!!!!!!!!
        for row in range(len(board)):
            for col in range(len(board[0])):
                DFS(row, col, trie.root)

        # Return the final answer
        return result