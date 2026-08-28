class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Creating various hashmaps to check for sudoku rules
        unordered_map<int, unordered_set<char>> rowChecker;
        unordered_map<int, unordered_set<char>> colChecker;
        unordered_map<int, unordered_set<char>> boxChecker;
       
        // Begin the board traversal
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                // Skipping the empty cells
                if (board[row][col] == '.') {
                    continue;
                }

                char currentCellValue = board[row][col];
                int boxID = (row / 3) * 3 + (col / 3);

                if (rowChecker[row].contains(currentCellValue)) {
                    return false;
                } else if (colChecker[col].contains(currentCellValue)) {
                    return false;
                } else if (boxChecker[boxID].contains(board[row][col])) {
                    return false;
                }

                rowChecker[row].insert(currentCellValue);
                colChecker[col].insert(currentCellValue);
                boxChecker[boxID].insert(currentCellValue);
            }
        }

        return true;
    }
};
