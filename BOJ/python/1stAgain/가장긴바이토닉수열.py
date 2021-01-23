# https://www.acmicpc.net/problem/11054

'''
< 최초 코드 >
* 먼저 가장 큰 값의 마지막 idx를 잡는다
* 그 마지막 idx 까지는, 증가하는 부분 수열
* 그 마지막 idx 이후부터는 감소하는 부분 수열을 구한다

* 마지막 idx 전까지는, 증가하는 부분 수열 이분탐색 함수
* 마지막 idx 후까지는 , 감소하는 부분 수열 이분탐색 

로컬 테스트에서는 아래의 코드가 작동했으나
백준에서는 시간초과로 인해 실패

n      = int(input())
arr    = list(map(int, input().split()))
answer = []
maxVal = max(arr)
MaxValLstIdx = (len(arr) - 1 ) - ( arr[::-1].index(maxVal) )
flagIdx = 0 

def findIncIdx(val):
    lt = 0
    rt = len(answer)
    res = 0 

    while lt <= rt :
        mid = ( lt + rt ) // 2

        if lt == rt :
            res = lt
            break
        elif val <= answer[mid] :
            rt = mid
        else:
            lt = mid + 1

    return res
            
    
def findDecIdx(val):
    lt = flagIdx
    rt = len(answer) - 1
    res = 0

    while lt <= rt :
        mid = ( lt + rt )  // 2
        if lt == rt :
            res = lt
        elif val >= answer[mid] :
            rt = mid
        else:
            lt = mid + 1

    return res


# 최대값의 마지막 까지는 계속 증가 수열로 구현하고,
# 해당 최대값을 넘어가고 나서는, lt를 해당 최대값 idx로 설정해서 다시 이분 탐색 
for idx, val in enumerate(arr) :
    if idx == 0 :
        answer.append(val)
        continue
    
    if idx < MaxValLstIdx :
        if val > answer[-1] :
            answer.append(val)
        else:
            newIdx = findIncIdx(val)
            answer[newIdx] = val

    elif idx == MaxValLstIdx :
        answer.append(val)
        flagIdx =  newIdx
        
    else : # 이제 decrease
        if val < answer[-1] :
            answer.append(val)
        else:
            newIdx = findDecIdx(val)
            answer[newIdx] = val

print(len(answer))

'''

n      = int(input())
a      = list(map(int, input().split()))
dInc   = [0 for i in range(n)]
dDec   = [0 for i in range(n)]
dFinal = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dInc[i] < dInc[j]:
            dInc[i] = dInc[j]
    dInc[i] += 1


# 팁 : 가장 긴 감소수열 > 가장 긴 증가수열 원리를, 배열 뒤에서부터 적용하면 된다.

for i in range( n - 1, -1, -1):
    for j in range( n - 1,i,-1):
        if a[i] > a[j] and dDec[i] < dDec[j]:
            dDec[i] = dDec[j]
    dDec[i] += 1


# 바이토닉 수열은, 해당 숫자를 기준으로 왼쪽은 증가수열 , 오른쪽은 감소 수열
# 왼쪽에서 오면서 구한 증가수열, 오른쪽에서 오면서 구한 증가수열 ( 사실 감소 수열 ) 값을 더하면
# 해당 값이 가운데에 있을 때 ,바이토닉 수열이며 그것의 길이
# 단, 자기 자신의 값이 2번 카운팅 되므로, 더한 길이의 값 - 1 을 해주어야 한다.

for i in range(n):
    dFinal[i] = dInc[i] + dDec[i] - 1

print(max(dFinal))
