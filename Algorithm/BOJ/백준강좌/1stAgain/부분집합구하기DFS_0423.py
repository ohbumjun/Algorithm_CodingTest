'''
1) 벽 정보 세팅
- 

2) 성에 있는 방의 개수 : bfs 및 dfs를 통한 집단 분류

3) 가장 넓은 방의 넓이 --> 위에서 구한 것 중에서 최댓값

4) 하나 벽 --> 벽 부수고 이동하기 

'''
n = int(input())

'''
1) 부분 수열의 개수 for 문 돌리기
2) 해당 부분 수열 갯수에 대한 dfs
'''


def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        # 사용한다, 사용하지 않는다 -> ch 활용하기
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


ch = [0] * (n+1)
DFS(1)
