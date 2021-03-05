# 

# 첫번째 풀이 : 오답
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dp(r1, c1, r2, c2) :
            
            # 갈 수 있는 방향이 없다면 
            if r1 > rowMax - 1 or c1 > colMax - 1 or r2 > rowMax - 1 or c2 > colMax - 1  :
                return 0
            
            # 어차피 r1 + c1 == r2 + c2 ( 결국, 마지막에는 같이 도달)
            # if r1 == c1 == n-1 :
            #    return grid[r1][c1]
            cur_cherry = 0
            
            if r1 == r2 and c1 == c2 :
                # 둘이 같은 곳에 도달해도 1개만 pick up
                cur_cherry = grid[r1][c1] 
            else :
                # 둘이 다른 곳에 있으면 둘다 pick up
                cur_cherry = grid[r1][c1] + grid[r2][c2]
                
            direction = [ (1,-1) , (1,0) , (1,1) ]
            
            next_cherry = 0
            
            for d1 in direction :
                for d2 in direction :
                    nr1 = r1 + d1[0]
                    nc1 = c1 + d1[1]
                    nr2 = r2 + d2[0]
                    nc2 = c2 + d2[1]
                    
                    next_cherry = max( next_cherry , dp(nr1,nc1,nr2,nc2) )
            
            # 즉, bottom_up 방식이다 
            cur_cherry += next_cherry 
            
            # 자. 만일 위에서 4개 경로 모두가 invalid한 경로라면, -sys.maxsize가 next_cherry로 return될 것이고
            # 이로 인해 cur_cherry도 매우 큰 '음수' 가 될 것이다 
            
            return cur_cherry 
        
        # 행
        rowMax = len(grid)
        # 열
        colMax = len(grid[0])
        
        ans = dp(0,0,0,colMax - 1)
        
        return ans 

# 두번째 풀이
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dp(row, c1, c2) :
            
            if (row,c1,c2) in memo.keys():
                return memo[(row , c1 , c2 )]

            cur_cherry = 0
            if c1 == c2 :
                # 둘이 같은 곳에 도달해도 1개만 pick up
                cur_cherry = grid[row][c1] 
            else :
                # 둘이 다른 곳에 있으면 둘다 pick up
                cur_cherry = grid[row][c1] + grid[row][c2]
                
            newCol = [ -1, 0, 1 ]
            next_cherry = 0
            
            for i in newCol :
                for j in newCol :
                    nc1 = c1 + newCol[i]
                    nc2 = c2 + newCol[j]
                    if row + 1 <= rowMax - 1 and 0 <= nc1 <= colMax - 1 and 0 <= nc2 <= colMax - 1  :
                        next_cherry = max( next_cherry , dp(row + 1,nc1,nc2) )
            
            # 즉, bottom_up 방식이다 
            cur_cherry += next_cherry 
            memo[(row,c1,c2)] = cur_cherry
            
            # 자. 만일 위에서 4개 경로 모두가 invalid한 경로라면, -sys.maxsize가 next_cherry로 return될 것이고
            # 이로 인해 cur_cherry도 매우 큰 '음수' 가 될 것이다 
            return cur_cherry 
        
        # 행
        rowMax = len(grid)
        # 열
        colMax = len(grid[0])
        memo = {}
        ans = dp(0,0,colMax - 1)
        
        return ans 