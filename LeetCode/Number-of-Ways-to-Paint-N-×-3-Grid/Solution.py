1class Solution:
2    def numOfWays(self, n: int) -> int:
3        mod=10**9+7
4        a=b=6
5        for _ in range(1,n):
6            a,b=(3*a+2*b)%mod,(2*a+2*b)%mod
7        return (a+b)%mod        