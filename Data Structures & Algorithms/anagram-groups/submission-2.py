class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creating a dictionary to hold the
        # group of words
        groups = {}

        # Go through each individual word in our list
        for word in strs:
            # Creating our key which is the word lexicographically
            # sorted
            key = ''.join(sorted(word))

            # Adding the key to our dictionary if it doesn't exist
            if key not in groups:
                groups[key] = []

            # Append the word to its given key
            groups[key].append(word)

        # Return the grouped anagrams
        return list(groups.values())