class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # make a set
        numberSet = set()
        
        # fill the set with the numbers
        for num in nums:
            numberSet.add(num)
        
        # check all numbers from 0...len(nums),
        # if it isn't in the set, it's the missing number
        for i in range(len(nums)+1):
            if i not in numberSet:
                return i
