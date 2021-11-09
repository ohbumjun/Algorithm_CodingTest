def partition2(S, low, high):
    '''
    pivot 을 어떻게 설정하느냐.도 매우 복잡하다

    그래서 여기서는 그저, 리스트의 첫원소를
    기준 원소로 정해보자 

    15 22 13 27 12 10 20 25 
    - pivot : 15

    결과적으로 아래와 같이 나누게 된다
    10 13 12 (15) 20 22 27 20 25

    이후에는
    10 13 12 ~ 20 22 27 20 25 
    에 대해서 재귀적으로 정렬을 수행한다

    다시 말해서 한번 pivot을 정한다는 것은,
    해당 pivot 만큼은, 자기 자신의 위치를 찾아가게 해준다는 것이고
    이후, 해당 pivot을 기준으로, 
    왼쪽을, 자기보다 무조건 작은 값들
    오른쪽은, 자기보다 무조건 큰 값들
    이 위치하게 된다.
    '''
    pivotitem = S[low]
    i = low + 1
    j = high'
    while(i <= j):
        while(S[i] < pivotitem):
            i += 1
        while(S[j] > pivotitem):
            j -= 1
        if(i < j):
            S[i], S[j] = S[j], S[i]  # swap
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]  # swap
    return pivotpoint

    def quicksort2(S, low, high):
        # low 부터 high 까지의 원소를 정렬하겠다 !
        # 따라서 low < high 일 경우에만, 정렬하는 경우에 해닫하는 것이므로
        # 아래와 같이 if low < high 라는 조건을 준 것이다
        if(high > low):
            # partition 된 pivot point를 받는다
        pivotpoint = partition2(S, low, high)
        # 해당 pivot 을 기준으로, 좌우, sorting 해준다
        quicksort2(S, low, pivotpoint - 1)
        quicksort2(S, pivotpoint+1, high)
