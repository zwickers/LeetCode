class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return index of first occurrence of needle in haystack
        # if the needle isn't in haystack, return -1
        return haystack.index(needle) if needle in haystack else -1
