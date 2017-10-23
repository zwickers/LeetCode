class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bin_list = []
        for i in range(num+1):
            bin_list.append(bin(i)[2:].count('1'))
        return bin_list
