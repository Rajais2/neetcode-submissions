class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creating a dict to hold all anagrams
        groups = {}

        # Begin traversing through each word in our list of strings
        for word in strs:
            # Sorting the word to act as our key
            key = ''.join(sorted(word))

            # Make sure the key exists before we append
            if key not in groups:
                groups[key] = []

            # Adding the word for that specifically lexicographically
            # sorted word
            groups[key].append(word)

        # Returning all grouped anagrams as a nested list
        return list(groups.values())