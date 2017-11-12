class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # O(n) time complexity
        # O(n) space complexity
        
        # KEYS: numbers from the nums list
        # VALUES: the respective indices of the numbers from the nums list
        buff_dict = {}
        
        # iterate through the nums list
        for i in range(len(nums)):
            # check if each element's complement (target - nums[i]) exists in the dict
            if (target - nums[i]) in buff_dict:
                # if it does, return the index of the current list element
                # and the index of it's complement
                return [i,buff_dict.get(target - nums[i])]
            # add each element's value and its index to the dict
            else:
                buff_dict[nums[i]] = i
