class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # use a dict to map characters to frequency
        counter = {}
        
        # increment the corresponding value for
        # each character in the dictionary
        for c in s:
            if c in counter:
                counter[c] = 1 + counter[c]
            else:
                counter[c] = 1
                
        # decrement the corresponding value for
        # each character in the dictionary
        for c in t:
            if c in counter:
                counter[c] = counter[c] - 1
            else:
                return False
            
        # if all the values in the dict are zero,
        # then the same characters are present in both
        # dictionaries, and therefore both strings
        # have the same characters and are anagrams
        for v in counter.values():
            if v != 0:
                return False
        return True
