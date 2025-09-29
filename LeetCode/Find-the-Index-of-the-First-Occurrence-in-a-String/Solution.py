class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index=-1
        index=haystack.find(needle)
        if index==-1:
            return -1
        else:
            return index