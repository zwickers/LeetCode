class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1 or s.count('LLL') >= 1:
            return False
        else:
            return True
