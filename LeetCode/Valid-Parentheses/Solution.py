class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p=[]
        q={'}':'{',']':'[',')':'('}
        for i in s:
            if i in q:
                if p and p[-1]==q[i]:
                    p.pop()
                else:
                    return(False)
            else:
                p.append(i)
        return(True) if not p else False
