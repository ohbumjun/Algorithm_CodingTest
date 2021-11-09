# https://leetcode.com/problems/cherry-pickup/submissions/

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dp(r1, c1, r2, c2) :
            n = len(grid)
            
            if( r1, c1, r2, c2) in memo :
                return memo[(r1,c1,r2,c2)]
            
            # 갈 수 있는 방향이 없다면 
            print(r1,c1,r2,c2)
            if r1 > n-1 or c1 > n-1 or r2 > n-1 or c2 > n-1 or grid[r1][c1] == -1 or grid[r2][c2] == -1 :
                return -sys.maxsize
            
            # 어차피 r1 + c1 == r2 + c2 ( 결국, 마지막에는 같이 도달)
            if r1 == c1 == n-1 :
                return grid[r1][c1]
            
            cur_cherry = 0
            
            if r1 == r2 and c1 == c2 :
                # 둘이 같은 곳에 도달해도 1개만 pick up
                cur_cherry = grid[r1][c1] 
            else :
                # 둘이 다른 곳에 있으면 둘다 pick up
                cur_cherry = grid[r1][c1] + grid[r2][c2]
                
            direction = [(1,0) ,(0,1)]
            
            # 0이라고 하면 안된다
            # 아래 dp(nr1, nc1, nr2, nc2) : arr[nr1][nc1] 까지의 최대 체리 개수 ( 끝 지점으로 부터 ) 가 -sys.maxsize를 리턴할 수 있는데 
            # 이것은 경로가 없다는 것이다. 
            # 우리는 next_cherry = max(next_cherry , dp(nr1,nc1,nr2,nc2)) 로 max 값을 갱신해오고 있으며
            # 그값을 cur_cherry += next_cherry 이와 같이 더해주고 있다
            # 그런데 우리는 결과적으로 cur_cherry를 통해서, r1,c1 에서 판단시 이후에 경로가 있는지 없는지를 판단해야 하는데 
            # 아무리 경로가 없는 경우에도 next_cherry 초기값 0 설정으로 인해 next_cherry는 0이상의 값이 리턴될 것이고
            # 그로 인해 cur_cherry라는 값을 기준으로, 이후 유효한 경로가 있는지 없는지 판단하기 힘들다는 것이다 
            next_cherry = -sys.maxsize
            
            for d1 in direction :
                for d2 in direction :
                    nr1 = r1 + d1[0]
                    nc1 = c1 + d1[1]
                    nr2 = r2 + d2[0]
                    nc2 = c2 + d2[1]
                    
                    next_cherry = max(next_cherry , dp(nr1,nc1,nr2,nc2))
            
            # 즉, bottom_up 방식이다 
            cur_cherry += next_cherry 
            memo[(r1,c1,r2,c2)] = cur_cherry 
            
            # 자. 만일 위에서 4개 경로 모두가 invalid한 경로라면, -sys.maxsize가 next_cherry로 return될 것이고
            # 이로 인해 cur_cherry도 매우 큰 '음수' 가 될 것이다 
            return cur_cherry 
        
        memo = {}
        n = len(grid)
        ans = dp(0,0,0,0)
        
        # 아래의 경로들이 모두 invalid하다면, 즉, invalid한 패턴이 있게 되면, 위의 경우에서 next_cherry 중 하나는 매우 큰 음수로 리턴
        # 그게 계속 bottom up 방식으로 올라오게 되어, ans 라는 최종 리턴값도  매우 큰 음수, 즉, 경로 없음으로 인식될 수 있다
        # 경로가 없는 경우에 대해서는 0 을 리턴한다 
        
        return ans if ans > 0 else 0