1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        list=[[0 for i in range(n)] for j in range(m)]
4        for i in range(0,n):
5            list[0][i]=1
6        for i in range(0,m):
7            list[i][0]=1
8        for i in range(1,m):
9            for j in range(1,n):
10                list[i][j]=list[i][j-1]+list[i-1][j]
11        return list[m-1][n-1]
12
13        