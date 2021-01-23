# https://www.acmicpc.net/problem/10844

# 풀이 링크 :https://suri78.tistory.com/91



n   = int(input())
mod = 1000000000
# stairs[idx] : 해당 idx 가 1의 자리수로 왔을 때 , 가능한 수의 개수
stairs = [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]

# 0은 , 이전 수가 1일때, 9는 이전 수가 8일때만 올 수 있고
# 그외는, idx - 1, idx + 1에서 올 수 있다
# 이러한 방식으로 계속 더해준다.

for _  in range(n - 1):
    tmp = stairs[:]
    # 0은 1에서 온다
    stairs[0] = tmp[1] % mod

    for i in range(1,9):
        stairs[i] = ( tmp[i+1]  + tmp[i-1] ) % mod

    # 9도 8에서만 온다
    stairs[9] = tmp[8] % mod

print(sum(stairs) % mod )
        


'''
DFS 로 푸는 방법

각 Level은 현재 자릿수 
Val은, 그곳에 들어갈 값

def DFS( N, val ):
    global cnt
    
    if N == num :
        cnt += 1
        return
    if N == 0 :
        for i in range(1,10):
            DFS( 1 , i )
    else:
        next = []
        if val - 1 >= 0 :
            next.append( val -1 )
        if val + 1 < 10 :
            next.append( val + 1 )

        for i in range(len(next)) :
            DFS( N + 1, next[i] )
                

num = int(input())
ch  = [0] * ( 101 )
cnt = 0
            
DFS(0,0)
print( cnt % 1000000000 )



'''

