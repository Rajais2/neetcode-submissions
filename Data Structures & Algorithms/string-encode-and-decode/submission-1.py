class Solution:
    def encode(self, strs: List[str]) -> str:
        intermediateList = []

        # Go through each string in our list
        for string in strs:
            # Get our current string's length
            length = len(string)

            # Append the string's length, the separator, and
            # the string itself
            intermediateList += [str(length) + "#" + string]

        # Return the final result as a string
        return "".join(intermediateList)
        
    def decode(self, s: str) -> List[str]:
        # Setting up a pointer
        position = 0
        
        # Setting up to store our result
        decodedStrings = []

        # Use a pointer to traverse the encoded string
        while position < len(s):
            # Getting the position of our separator
            separatorIdx = s.find("#", position)

            # Get the length of the current string we're on
            curStringLength = int(s[position:separatorIdx])

            # Add the string to our decoded list of strings
            decodedStrings.append(s[separatorIdx + 1:separatorIdx + 1 + curStringLength])

            # Updating our position
            position = separatorIdx + 1 + curStringLength

        # Returning our final list of decoded strings
        return decodedStrings

            


