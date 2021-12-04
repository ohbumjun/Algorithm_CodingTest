def shell_sort(arr):
    # 삽입 정렬과 같은 원리 적용
    # 즉, gap 거리에 위치해 있는 요소들은,
    # 정렬 이후, 정렬되어 있어야 한다.
    size = len(arr)
    for i in range(len(arr) // 2, size):
        anchor = arr[i]
        j = i
        # anchor 의 원소와
        # arr[j - gap] 의 원소를 서로 비교할 것이다
        while j >= gap and arr[j-gap] > anchor:
            arr[j] = arr[j-gap]
            j -= gap
        # 즉, 계속 오른쪽으로 옮겨두고
        # 처음에 있던 anchor의 값을, j의 바뀐 위치에 넣는다
        arr[j] = anchor

    # gap은 매 단계마다 2로 나눠가면서 적용해간다
    gap = gap // 2


n = int(input())
arr = list(map(int, input().split()))
