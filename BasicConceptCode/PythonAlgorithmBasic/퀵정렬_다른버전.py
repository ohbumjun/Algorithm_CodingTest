def quicksort(S, low, high):
    # low 부터 high 까지의 원소를 정렬하겠다 !
    # 따라서 low < high 일 경우에만, 정렬하는 경우에 해닫하는 것이므로
    # 아래와 같이 if low < high 라는 조건을 준 것이다
    if(high > low):
        pivotpoint = partition(S, low, high)
        quicksort(S, low, pivotpoint - 1)
        quicksort(S, pivotpoint+1, high)


def partition(S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low+1, high+1):
        # pivotitem 보다 작은 애를 만나면
        if(S[i] < pivotitem):
            # j를 1 증가시키고
            j += 1
            # i, j를 swap 시킨다
            # j는 생각해보면 i가 자연스럽게 지나쳐온 값일 것이다
            # 즉, pivotitem보다 큰 값이라는 것
            # 이 과정을 통해 pivotitem보다 큰, 작은, 값을 서로 바꿔줄 수 있는 것이다
            S[i], S[j] = S[j], S[i]  # swap
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]  # swap
    return pivotpoint
