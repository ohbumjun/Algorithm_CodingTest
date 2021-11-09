n, m = map(int, input().split())
arr = list(map(int, input().split()))
cal = ['+', '-']
ans = -1


def dfs(L, res):  # ++-
    global ans
    if L == n-2:
        tmp = arr[0]
        for i in range(len(res)):
            if res[i] == '-':
                tmp -= arr[i+1]
            else:
                tmp += arr[i+1]
        if tmp == m:
            ans = 1
        return
    else:
        for i in range(2):
            dfs(L+1, res + str(cal[i]))  # dfs(2,+++)


for i in range(2):
    dfs(0, str(cal[i]))

print("YES" if ans == 1 else "NO")
