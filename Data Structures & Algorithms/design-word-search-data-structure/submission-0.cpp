class WordDictionary {
private:
    // Creating a structure to represent a node
   struct Node {
        // Our children can be any alphabetical character 
        Node* children[26];

        // Creating a isEnd bool flag to mark the end of a word
        bool isEnd;

        // Node constructor
        Node() {
            // It is not the end of a word
            isEnd = false;

            // It does not have any children
            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
        }  
    };

    Node* root;

public:
    bool DFS(Node* curNode, string& word, int index) {
        // If we have fully covered the word, return the 
        // isEnd flag
        if (index == word.size()) {
            return curNode->isEnd;
        }

        // If our character is a normal character, do a single path DFS
        if (word[index] != '.') {
            // Convert to index
            int charIndex = word[index] - 'a';

            // Stop if that child doesn't exist
            if (curNode->children[charIndex] == nullptr) {
                return false;
            }

            // Otherwise, recurse to that children and onto the
            // next part of our word
            return DFS(curNode->children[charIndex], word, index + 1);
        }

        // Only executes if our character is a wildcard
        // Bascially have to check all possibilities
        for (int i = 0; i < 26; i++) {
            // If that child node does exist, explore that path
            if (curNode->children[i] != nullptr) {
                // If that path works, then return true
                if (DFS(curNode->children[i], word, index + 1)) {
                    return true;
                }
            }
        }

        // Otherwise, we have exhausted all options, meaning
        // nothing was found
        return false;
    }
    
    WordDictionary() {
        // Creating our new prefix tree
        root = new Node();        
    }
    
    void addWord(string word) {
        // Storing our current position in the tree
        Node* currentNode = root;

        // Traversing through each character of the word
        for (int i = 0; i < word.size(); i++) {
            // Converting to index
            int charIndex = word[i] - 'a';

            // If the child node doesn't exist, create it and move forward
            if (currentNode->children[charIndex] == nullptr) {
                currentNode->children[charIndex] = new Node();
                currentNode = currentNode->children[charIndex];
            } else {
                // Otherwise, simply just move forward
                currentNode = currentNode->children[charIndex];
            }
        }

        // Mark the final node we visit isEnd flag as true
        currentNode->isEnd = true;
    }
    
    bool search(string word) {
        // Utilizing our DFS function to perform our search
        if (DFS(root, word, 0)) {
            return true;
        }

        // No path was found, so we return false
        return false;
    }
};
