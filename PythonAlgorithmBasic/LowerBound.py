# https://m.blog.naver.com/PostView.nhn?blogId=bestmaker0290&logNo=220820005454&proxyReferer=https:%2F%2Fwww.google.com%2F

'''
Lower Bound 란,
원하는 k 값 이상이 처음 나오는 위치를 찾는 과정.을 의미한다.
즉, 찾고 싶은 k 값과 같은 값이 나타나는 첫위치를 찾거나
같은 값이 없으면, 큰 값이 나타나는 첫 위치를 찾는 방법이다.
'''

'''
Lower Bound를 먼저 살펴보자.
< 정렬된 데이터 {1, 3, 5, 7, 9, 11}에서, 8 이상인 값이 처음 나오는 위치를 구하는 과정 >

1) 시작위치 = 1, 끝위치 = 6 설정
2) 시작 위치 1과, 끝 위치 6의, 중간 위치 3 > 5와 8을 비교한다
3) 5는 8보다 작으므로, 시작위치를 중간위치 + 1 인, 4로 설정한다
4) 시작 위치 4와, 끝 위치 6의 중간 위치인 5 > 9와 8을 비교한다
5) 8은 9보다 작으므로, 끝위치를 중간위치로 설정한다( end = mid)
- 보통 이진 탐색에서는, 원하는 값을 찾아나가는 과정이므로, 
end = mid - 1을 한다. 
- 하지만, lower bound는 원하는 값 k 이상이 처음 나오는 위치를 찾는 과정이다.
다시 말해서, end도 지금은 비록 mid보다 크지만
원하는 값 k 이상이 처음 나오는 위치가 될 수 있다는 것이다
6) 7은 8보다 작다. 따라서, 시작 위치를 1증가시켜서 9에 놓는다
7) 시작위치와, 끝 위치가 같아졌다. 결국 9가 lower_bound
즉, 원하는 값 8 이상이 나오는 처음 위치가 된다.

'''

def lower_bound(start, end ,num) :
    while start < end :
        mid = ( start + end ) // 2
        if res[mid] == num:
            end = mid
        elif res[mid] < num :
            start = mid + 1
        else:
            end = mid
    
    # 결국 start == end 일때 break 하게 된다
    return end
