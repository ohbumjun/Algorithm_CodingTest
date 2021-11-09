# https://leetcode.com/problems/knight-probability-in-chessboard/

# 첫번째 풀이 : Graph ( BFS )

class Solution:

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        def Neighbor(row, col, L, N):
            dCol = [-2, -1,  1, 2, 2, 1, -1, -2]
            dRow = [-1, -2, -2, -1, 1, 2,  2,  1]
            finalL = []
            for i in range(8):
                newCol = col + dCol[i]
                newRow = row + dRow[i]
                if 0 <= newRow < N and 0 <= newCol < N:
                    finalL.append((newCol, newRow))

            return finalL

        kp = 1/8
        res = 0
        queue = deque([(r, c, 0, 1)])
        # r, c, currentMove, currentP
        while len(queue):
            q = queue.popleft()
            curRow, curCol, curMove, curP = q
            if curMove == K:
                res += curP
            else:
                for newP in Neighbor(curRow, curCol, curP, N):
                    newCol, newRow = newP
                    queue.append((newRow, newCol, curMove + 1,  curP * kp))
        print(res)
        return res

# Time : 8 ^ k
# Space : 8 ^ k ( Neighbor 함수에 의해, 한 이동마다 디동가능한 8개의 경로가 생긴다 )


# 두번째 풀이 : DP
'''
기본 원리 : 해당 idx 까지 도달할는 경우 : 주변 8칸에서 해당 요소까지 가는 방법

주변 8칸까지 가는 확률 * 1/8 들을 더한 값 : 해당 idx까지 도달할 확률

N * N 원리로
이중 반복문을 돌면서
접근하면 된다

그리고 각 차수
즉 각 이동 때마다
N * N , 확률 정보를 담은 
배열을 update 시켜주면 된다

'''


class Solution:

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        def Neighbor(row, col, N):
            dCol = [-2, -1,  1, 2, 2, 1, -1, -2]
            dRow = [-1, -2, -2, -1, 1, 2,  2,  1]
            finalL = []
            for i in range(8):
                newCol = col + dCol[i]
                newRow = row + dRow[i]
                if 0 <= newRow < N and 0 <= newCol < N:
                    finalL.append((newCol, newRow))

            return finalL

        '''
        각 구간에서 해당 영역까지 갈 수 잇는 
        개수 * 기존 memeo에 저장된 값
        
        n*n 한번 다 돌고나면
        memo를 update 한다
        '''

        kp = 1/8
        memo = [[0] * N for _ in range(N)]
        res = 0
        memo[r][c] = 1

        for _ in range(K):
            newMemo = [[0] * N for _ in range(N)]
            for cr in range(N):
                for cc in range(N):
                    for newL in Neighbor(cr, cc, N):
                        newCol, newRow = newL
                        newMemo[cr][cc] += memo[newRow][newCol] * kp
            memo = newMemo

        for row in memo:
            res += sum(row)

        return res

# Time : O ( K * N^2 )
# Space : N * N
