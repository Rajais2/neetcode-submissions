class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Will hold the longest common prefix
        result = ""        

        # Use a reference string to do comparsions
        for i in range(len(strs[0])):
            # Loop through the rest
            for string in strs:
                if i >= len(string) or string[i] != strs[0][i]:
                    return result

            result += strs[0][i]

        return result