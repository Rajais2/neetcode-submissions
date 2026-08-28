class Solution {
public:
    vector<string> result;

    void backtrack(vector<char>& path, int n, int openParanCount, int closeParanCount) {
        if (path.size() == 2 * n) {
            string currentStr = string(path.begin(), path.end());
            result.push_back(currentStr);
            return;
        }

        if (openParanCount < n) {
            path.push_back('(');
            openParanCount++;
            
            backtrack(path, n, openParanCount, closeParanCount);
            path.pop_back();

            openParanCount--;
        }

        if (closeParanCount < openParanCount) {
            path.push_back(')');
            closeParanCount++;
            
            backtrack(path, n, openParanCount, closeParanCount);
            path.pop_back();

            closeParanCount--;
        }
    }
    
    vector<string> generateParenthesis(int n) {
        vector<char> path;
       
        backtrack(path, n, 0, 0);

        return result;
    }
};
