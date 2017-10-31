class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip()) == 0:
            return 0
        else:
            # by default, split() seperates based on whitespace
            return len(s.strip().split())
