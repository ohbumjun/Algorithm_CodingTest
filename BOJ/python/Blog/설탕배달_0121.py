# https://www.acmicpc.net/problem/2839


# 1. '설탕kg'을 입력받는다.
# 2. 봉지개수 변수 count 선언
# 3. while문을 계속 돈다
#   1) 입력받은 '설탕kg'이 5로 정확히 나누어떨어진다면, 그 몫을 count에 더해 출력한다
#   2) 나누어떨어지지 않으면 '설탕kg' -= 3 을 해주고
#   3) count += 1 증가. 왜 ? 3kg 봉지를 하나 사용한 것이므로
#   4) 만약 계속 빼다가 '설탕kg'이 < 0 하다면, 3, 5 kg 의 봉지 조합으로 담을 수 없는 무게이므로 -1 출력

Honey = int(input())
cnt = 0

while True :
    if ( Honey % 5 == 0 ) :
        cnt = cnt + ( Honey // 5 )
        print(cnt)
        break

    Honey -= 3
    cnt += 1

    if Honey < 0 :
        print(-1)
        break
        

