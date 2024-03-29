# https://www.acmicpc.net/problem/2579

if __name__ == "__main__" :
    n   = int(input())
    dy  = [0] * ( n + 1 )
    arr = [0] * ( n + 1 ) 

    for i in range(1,n+1):
        arr[i] = int(input())

    dy[1] = arr[1]
    dy[2] = arr[1] + arr[2]
    # 여기서 중요한 것은, 연속으로 3 계단을 밟으면 안된다는 것이다
    # 또한, 무조건, 마지막 계단은 밟아야 한다
    # Top-Down 방식으로 접근할 것인데, 마지막 계단을 밟는 다는 것은, 무조건 마지막 arr[n]은 더해주게 설정해야 한다는 것이다
    # 그렇다면, 우리가 고려할 것은, 바로 이전의 계단을 밟았느냐 안밟았느냐
    # 1) 바로 이전 계단을 밟았다 == 2개 이전 계단은 밟으면 안되고, 3개 이전 계단에서 2단계 점프하여, 이전 계단을 밟음
    # code : arr[i] + arr[i-1] + dy[i-3]
    # 2) 이전 계단을 밟지 않았다 == 2개 이전 계단 밟고 , 2단계 점프했다
    # code : arr[i] + dy[i-2] 

    for i in range(3, n + 1):
        dy[i] = max( arr[i] + arr[i-1] + dy[i-3] , arr[i] + dy[i-2] )

    print(dy[n])
