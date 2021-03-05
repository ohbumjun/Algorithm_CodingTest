# 

# 1. DFS : Time Limit --------
class Solution(object):
    
    def __init__ (self):
        self.cnt = 0
        self.dCol = [ 1, 0]
        self.dRow = [ 0, 1]
    
    def dfs(self, row, col,m,n, ch ): # row : 행, col : 열
 
            if row == m - 1 and col == n - 1 :
                self.cnt += 1
                return
            else:
                for i in range(2):
                    nRow = row + self.dRow[i]
                    nCol = col + self.dCol[i]
                    
                    if 0 <= nRow < m and 0 <= nCol < n and ch[nRow][nCol] == 0 :
                        # 체크
                        ch[nRow][nCol] = 1
                        self.dfs( nRow , nCol,m,n,ch )
                        ch[nRow][nCol] = 0
                        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cnt = 0
        
        # dfs : ch 리스트 만들기
        # m : 행
        # n : 열
        
        
        ch = [ [0] * n for _ in range(m) ]
        ch[0][0] = 1
        self.dfs(0,0,m,n,ch)
        
        return(self.cnt)
        
# 2. DP ( Top - Down )
class Solution(object):
    
                        
    def uniquePaths(self, m, n):  # m : row , n : col 
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dis = [ [0] * n for _ in range(m) ]
        
        if m ==1 and n == 1:
            return 1

        # 세로 세팅
        for i in range(len(dis) - 2, -1, -1) : # 행의 길이
            dis[i][-1] = 1

        # 가로 세팅
        for i in range(len(dis[0]) - 2 , -1, -1 ) : # 열의 길이
            dis[-1][i] = 1

        # 1.1 부터 시작하여 목적지까지 ( 오른쪽, 아래에서 가능 )
        for i in range( len(dis) - 2, -1 , -1 ) : # 행 
            for j in range( len(dis[0]) - 2, -1, -1 ) : # 열 
                dis[i][j] = ( dis[i+1][j] ) + ( dis[i][j+1]  )
        
        return(dis[0][0])
