class Solution {
public:
    // Creating our cardinal directions to simplify code
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    void DFS(vector<vector<char>>& board, int row, int col) {
        // Bounds checking
        if (row < 0 || row >= board.size() || col < 0 || col >= board[0].size()) {
            return;
        } else if (board[row][col] != 'O') {
            // Simply quit if the cell is not an O
            return;
        }

        // Marking this cell as safe/able to escape
        board[row][col] = '#';

        // Begin checking all four-directionally connected groups
        for (int i = 0; i < dx.size(); i++) {
            // Exploring all other cells
            DFS(board, row + dx.at(i), col + dy.at(i));
        }
    }
    
    void solve(vector<vector<char>>& board) {
        if (board.empty()) {
            return;
        }
        
        // Idea: traverse all border cells and check if it is an 'O'
        // If it is, DFS from that point on
        for (int i = 0; i < board[0].size(); i++) {
            // Top row
            if (board[0][i] == 'O') {
                DFS(board, 0, i);
            }

            // Bottom row
            if (board[board.size() - 1][i] == 'O') {
                DFS(board, board.size() - 1, i);
            }
        }

        for (int i = 0; i < board.size(); i++) {
            // Left column
            if (board[i][0] == 'O') {
                DFS(board, i, 0);
            }

            // Right column
            if (board[i][board[0].size() - 1] == 'O') {
                DFS(board, i, board[0].size() - 1);
            }
        }

        // Begin traversing our entire board to check unsafe cells
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                // These cells are safe so we revert them back
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    // These cells aren't so we convert them
                    board[i][j] = 'X';
                }
            }
        }
    }
};
