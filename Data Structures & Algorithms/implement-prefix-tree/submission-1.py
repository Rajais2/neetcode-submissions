# Creating a class to represent an
# individual Trie Node
class TrieNode:
    def __init__(self) -> None:
        # A Trie Node should know its children
        # and if it is the end of a word
        self.children = {}
        self.isWord = False

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
        current.isWord = True

    def search(self, word: str) -> bool:
        # Set up a current pointer starting at the root
        current = self.root

        # Traverse through each character
        for character in word:
            # If the character doesn't exist, we
            # know the word doesn't exist
            if character not in current.children:
                return False
            else:
                # Move our current pointer to that character
                current = current.children[character]

        # Checking if our final spot is a word
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        # Set up our current pointer again
        current = self.root

        # Traverse through our prefix
        for character in prefix:
            # If the character doesn't exist, it is
            # not a prefix
            if character not in current.children:
                return False
            else:
                # Move our currnet pointer
                current = current.children[character]

        # We have traversed the entire prefix, so
        # it exists
        return True

        