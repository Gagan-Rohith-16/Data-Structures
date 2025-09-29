class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        r=nums.count(val)
        while(r!=0):
            nums.remove(val)
            r-=1
        return len(nums)      