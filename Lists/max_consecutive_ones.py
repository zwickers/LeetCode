class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # solution with O(n) time complexity
        # and O(1) space complexity
        
        count = 0
        ans = 0
        for num in nums:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                # reset counter if num != 1
                count = 0
        return ans
