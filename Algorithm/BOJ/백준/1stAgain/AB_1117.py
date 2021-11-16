# https://www.acmicpc.net/problem/12970

n , k = map(int,input().split())

# 쌍의 개수를 구한다 
def check(word):
    cnt = 0
    for i in range(len(word)-1):
        if word[i] == 'A':
            for j in range(i+1,len(word)):
                if word[j] == 'B':
                    cnt += 1
    return cnt

a = 'B'*n
a = list(a)
# 앞에서부터 A를 채워나간다 
for i in range(n):
    a[i] = 'A'
    if check(a) == k:
        break
    elif check(a) > k:
        a[i] = 'B'

t = "".join(a)
if t=='B'*n or t=='A'*n:
    if k == 0:
        print(t)
    else:
        print(-1)
else:
    print(t)