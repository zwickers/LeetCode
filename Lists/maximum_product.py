class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # clever solution with
        # O(n) time complexity
        # using a heap
        
        three_largest = heapq.nlargest(3,nums)  # O(nlog3) = # O(n) 
        
        # need to keep track of two smallest
        # to account for negative numbers
        two_smallest = heapq.nsmallest(2,nums)  # O(nlog2) = # O(n)
        
        return max(three_largest[0]*three_largest[1]*three_largest[2],two_smallest[0]*two_smallest[1]*three_largest[0])
