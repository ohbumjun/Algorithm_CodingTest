def DFS(L, val):
    if L == m :
        print(' '.join(map(str,res)))
        return
    else:
        # 같은 DFS 레벨 상에서, 같은 값이 들어가는 것을 방지 ex. 1, 9 이후, 또 1,9 가 들어가는 것 방지
        # arr은 sort되어 있다. 즉, 앞에서부터 1, 7, 9, 9 이런식으로 arr이 들어온다
        # 만약 앞의 9가 한번 쓰였고, 그 다음 9에 접근할 때, overlap != arr[i] 에 걸려서 넘어가게 된다
        # ( 질문 : 1 9 7 9  > 이런식이면 overlap은 의미없는 거잖아  ???  > 그래서 아래서 arr.sort() 해준  거라고 ;;)
        overlap = 0
        for i in range( n ):
            # 체크 안된애만 들어간다
            if ch[i] == 0 and overlap != arr[i]:
                #체크 표시
                ch[i] = 1
                # 배열에 넣기
                res[L] = arr[i]
                # 같은 L 상에서, 중복 요소 사용제거
                overlap = arr[i]
                # DFS
                DFS( L + 1 , i + 1)
                # 다시 체크 해제
                ch[i] = 0 

if __name__ == "__main__" :
    
    n,m = map(int,input().split())

    arr = list(map(int,input().split()))
    ch  = [0] * (n+1)
    res = [0] * m
    arr.sort()

    DFS(0,0)
