class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = list("aeiouAEIOU")
        # to traverse from the beginning of the list
        l = 0
        # to traverse from the end of the list
        r = len(s) - 1
        s = list(s)
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            # swap the two vowels
            s[l], s[r] = s[r], s[l]
            # move the pointers
            l += 1
            r -= 1
        return "".join(s)
