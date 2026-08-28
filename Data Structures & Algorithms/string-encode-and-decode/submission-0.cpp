class Solution {
public:

    string encode(vector<string>& strs) {
        // Setting up to store the final result
        string finalResult = "";

        // Encoding our string by first appending the length, then a hashtag, and then the string itself
        for (string str : strs) {
            finalResult += to_string(str.size()) + "#" + str;
        }

        // Return the encoded string
        return finalResult;
    }

    vector<string> decode(string s) {
        // Setting up to store the decoded result
        vector<string> result;
        int i = 0;

        // Traversing through the encoded string
        while (i < s.size()) {
            // Setting up to parse the data
            int j = i;

            // Continue until we reach our delimiter (#)
            while (s[j] != '#') {
                j++;
            }
            
            // Getting the length of our specific word by taking the substring and then move past
            int length = stoi(s.substr(i, j - i));
            j++;

            // Extract the word itself and insert it back
            string word = s.substr(j, length);
            result.push_back(word);

            // Push our position forward
            i = j + length;
        }

        // Return the final decoded result
        return result;
    }
};
