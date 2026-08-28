class PrefixTree {
private:
   // Creating a structure to represent a node
   struct Node {
        Node* children[26];
        bool isEnd;

        Node() {
            isEnd = false;

            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
        }  
    };

    // Creating a node pointer to represent the tree's root
    Node* root;

public:
    PrefixTree() {
       // Creating a new empty tree
       root = new Node(); 
    }
    
    void insert(string word) {
        // Storing our position at the root for traversal
        Node* currentNode = root;

        // Traverse through each character of our word
        for (int i = 0; i < word.size(); i++) {
            // Converting our character to an index
            int charIndex = word[i] - 'a';

            // If the child at that specific position doesn't exist,
            // create it
            if (currentNode->children[charIndex] == nullptr) {
                currentNode->children[charIndex] = new Node();
                currentNode = currentNode->children[charIndex];
            } else {
                currentNode = currentNode->children[charIndex];
            }
        }

        // Marking the end of the word
        currentNode->isEnd = true;
    }
    
    bool search(string word) {
        // Storing our position at the root for traversal
        Node* currentNode = root;

        for (int i = 0; i < word.size(); i++) {
            int charIndex = word[i] - 'a';

            if (currentNode->children[charIndex] == nullptr) {
                return false;
            } else {
                currentNode = currentNode->children[charIndex];
            }
        }

        if (currentNode->isEnd == true) {
            return true;
        }

        return false;
    }
    
    bool startsWith(string prefix) {
        Node* currentNode = root;

        for (int i = 0; i < prefix.size(); i++) {
            int charIndex = prefix[i] - 'a';

            if (currentNode->children[charIndex] == nullptr) {
                return false;
            } else {
                currentNode = currentNode->children[charIndex];
            }
        }

        return true;
    }
};
