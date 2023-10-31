# https://www.acmicpc.net/problem/10830

from copy import deepcopy

N,B        = map(int,input().split())
f_matrix   = [list(map(int,input().split())) for _ in range(N)]
c_matrix   = deepcopy(f_matrix)

divided = []

# 시간초과 방지를 위해, 반반씩 곱해가는 원리를 적용해갈 것이다
# 예를 들어, B가 8이라면, 8번 행렬을 곱하는 것이 아니라
# A^1, A^2, A^4, A^8 이런 식으로 곱하는 단계를 간소화 할 것이다 
tmp = B

# 2로 나눈 몫들을 구해간다 
while tmp >= 1 :
    divided.append(tmp)
    tmp = tmp // 2
divided.sort()

def calMat(finalM,mulM):
    n_matrix = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            num = 0
            for i in range(N):
                num += finalM[r][i] * mulM[i][c]
            n_matrix[r][c] = num % 1000
    return n_matrix

# 다음의 값은, 이전의 값 *2 혹은 *2 + 1 이기 때문에
# 이에 맞춰서, 다음 곱할 행렬을 구해간다 
l_divided = len(divided)
for i in range(l_divided-1):
    curN = divided[i]
    nxtN = divided[i+1]
    tmp_matrix = calMat(c_matrix,c_matrix)
    if nxtN == curN * 2:
        c_matrix = tmp_matrix
    else :
        c_matrix = calMat(tmp_matrix,f_matrix)
        
# 1000 으로 나눈 나머지를 각 원소에 저장하기 : 안하면 80% 에서 오류
for r in range(N):
    for c in range(N):
        c_matrix[r][c] %= 1000

for i in range(N):
    print(' '.join(map(str,c_matrix[i])))
    
