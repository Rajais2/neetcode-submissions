class Solution {
public:
    bool DFS(vector<vector<char>>& board, string word, int row, int col, int index) {
        // We have found a path!
        if (index == word.size()) {
            return true;
        }

        // Bounds checking
        if (row < 0 || row >= board.size() || col < 0 || col >= board[0].size()) {
            return false;
        }

        // Getting the original charcter for restoration purposes
        auto originalCharacter = board[row][col];

        // If the current cell matches a part of the word, mark the cell
        // as visited and explore the adjacent cells
        if (board[row][col] == word[index]) {
            board[row][col] = '#';
            
            if (DFS(board, word, row - 1, col, index + 1)) {
                return true;
            } else if (DFS(board, word, row + 1, col, index + 1)) {
                return true;
            } else if (DFS(board, word, row, col - 1, index + 1)) {
                return true;
            } else if (DFS(board, word, row, col + 1, index + 1)) {
                return true;
            }

            // Here, we undo our recursion and restore the cell
            // to its original contents
            board[row][col] = originalCharacter;
        } 

        // Return false as all paths have been exhausted
        return false;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        // If the word is empty, then we always have a path
        if (word.empty()) {
            return true;
        }

        // Traverse through the board
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                // Checking if we can find a path
                if (DFS(board, word, row, col, 0)) {
                    return true;
                }
            }
        }

        // We have traversed through the entire board, meaning we didn't
        // find a path
        return false;
    }
};