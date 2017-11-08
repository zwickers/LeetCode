class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # This can be trivially solved using a list comprehension
        
        alphabet = string.ascii_lowercase # "abcde....xyz"
        
        indices = [s.index(c) for c in alphabet if s.count(c) == 1]
        
        if len(indices) > 0:
            return min(indices)
        else:
            return -1
