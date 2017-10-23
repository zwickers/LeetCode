class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        
        # this will work even when the length
        # of s is 0 (empty string), because
        # the while loop will never be entered
        # and the method will simply return True
        while l < r:
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower()==s[r].lower():
                        # continue working towards
                        # the middle of the string
                        l += 1
                        r -= 1
                else:
                    return False
        return True
