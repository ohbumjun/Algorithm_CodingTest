# while문 사용하기
def BS(st, ed, target):
    while st <= ed:
        mid = (st + ed) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            ed = mid - 1
        else:
            st = mid + 1


def BS(st, ed):
    while st <= ed:
        mid = (st + ed) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return BS(mid + 1, ed)
        else:
            return BS(st, mid - 1)


Len, target = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(BS(0, len(arr) - 1))
