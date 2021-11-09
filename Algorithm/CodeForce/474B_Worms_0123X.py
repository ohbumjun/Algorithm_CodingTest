
# 첫번째 풀이 : 이분 탐색---------------------------------
'''
< 기본적인 원리는 다음과 같다 >

2단계의 이분탐색을 진행할 생각이었다
1. 현재 num가 몇번째 타일에 있는지
2. 그 타일에서, 몇번째에 있는지

하지만, 2. 절차는 필요 없다.
그래서 1. 절차, 몇번째 타일에 있는지만 보면된다.

그렇다면 어떻게 하느냐 ?
각 타일의 처음숫자, 마지막 숫자 정보를 저장해두고
입력되는 숫자가 그 타일에 해당하는지를 비교할 때,
처음숫자, 마지막 숫자 끼리의 비교를 진행하면 된다.

처음 숫자는, 이전 타일의 마지막 숫자 + 1,
마지막 숫자는, 이전 타일 마지막 숫자 + 현재 들어온 숫자

여기까지는 좋았고,

binSearch 함수도 잘 짰다.

단 !!!
입력숫자가 천문학적으로 많아질 때 , 
모든 입력숫자에 대해 일일히 binSearch를 진행한다면
Run Time Error가 뜬다.

'''
def BinS(st, ed, taget) :
    if st > ed :
        return
    else:
        mid = ( st + ed ) // 2

        if dy[mid] - arr[mid] <= target and target <= dy[mid] :
            return mid
        elif target < dy[mid] - arr[mid] :
            return BinS(st, mid - 1, target)
        elif target > dy[mid] + arr[mid] :
            return BinS( mid + 1 , ed, target ) 

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))
dy = [0] * ( n )
dy[0] = arr[0]

for i in range(1, n):
    dy[i] = arr[i] + dy[i-1]

for target in targets :
    print(BinS(0, len(arr) - 1, target) + 1)


# 2번째 풀이 : DP ?? -----------------------------------------
'''
제일 좋은 것은
값을 입력받으면서 동시에
현재 숫자가 몇번째 그룹에 해당하는지도 같이 저장하는 것이다. 
'''
n = int(input())
arr = list(map(int,input().split()))
groups = []
group = 0

for i in range(len(arr)) :
    group += 1
    for i in range(arr[i]) :
        groups.append(group)

m = int(input())
targets = list(map(int,input().split()))
for target in targets :
    # -1 을 해주는 이유는 ? 예를 들어, groups 에서 '1'이라는 숫자의 group은 groups[0] 이라는 0 인덱스에 저장되어 있으므로
    print(groups[target - 1])
