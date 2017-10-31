class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reverse the letters of each word in a sentence
        words = s.split(" ")
        words = [word[::-1] for word in words]
        return " ".join(words)
