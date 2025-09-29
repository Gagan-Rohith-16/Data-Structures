class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        r=list(str(x))
        r.reverse()
        m=str(x)
        v=''.join(i for i in r)
        return v==m