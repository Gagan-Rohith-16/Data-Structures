class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=[]
        a=0
        if len(s)>2:
            for i in s:
                if(i not in r):
                    r.append(i)
                    if(a<len(r)):
                        a=len(r)
                elif(i in r):
                    if(a<len(r)):
                        a=len(r)
                    del r[:r.index(i)+1]
                    r.append(i)
            return a
        elif len(s)==0:
            return 0
        elif len(s)==2 and s[0]!=s[1]:
            return 2
        else:
            return 1