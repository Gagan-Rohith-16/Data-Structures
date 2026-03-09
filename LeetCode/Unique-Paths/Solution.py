1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        list=[[0 for i in range(n)] for j in range(m)]
4        i,j=0,0
5        for i in range(0,n):
6            list[0][i]=1
7        for i in range(0,m):
8            list[i][0]=1
9        for i in range(1,m):
10            for j in range(1,n):
11                list[i][j]=list[i][j-1]+list[i-1][j]
12        return list[i][j]
13
14        