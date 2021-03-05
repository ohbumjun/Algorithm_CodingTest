# https://codeforces.com/problemset/problem/1348/A
# " Phoenix and Balance "
n  = int(input())
    
for i in range(n):
    
    numCoin = int(input())
        
    a = 0
    b = 0

    # 제일 큰 숫자를 a 에 넣는다
    a += 2 ** numCoin

    # 작은 숫자부터 n//2 - 1 개 a에 더한다
    # - 1을 해주는 이유는, 이미 제일 큰 숫자를 더했으므로 더하는 횟수에서 -1
    # 뿐만 아니라, 2개가 동일한 갯수로 나눠져야 하므로 numCoin // 2 를 해준다 
    # 동시에, 나눠진 합끼리의 차이가 최소 ?
    for i in range(1, numCoin // 2 ):
        a += 2 ** i
        
    for i in range( numCoin // 2, numCoin ):
        b += 2 ** i

    print(abs(a-b))
                