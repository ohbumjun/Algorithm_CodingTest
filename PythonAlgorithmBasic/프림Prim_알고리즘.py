#

'''
프림 알고리즘의 원리는 다음과 같다.
임의의 시작점 하나를 잡는다.

해당 점과 거리가 가장 가까운 정점을 선택해가는 과정을 거친다.

모든 정점들의 집합을 V라고 하자.
Y : 선택된 노드의 집합
V - Y : 선택되지 않은 노드의 집합.

Y 의 노드 ~ V- Y 의 노드. 들의 연결 중
거리가 최소인 노드들을 선택해가는 것이다.

nearest[i]
distance[i]
라는 배열을 선언할 것이다. 

nearest[i]는, 최근 선택한, 
Y에 최근 추가한 노드를 의미한다. 

distance[vnear] 는 
해당 노드 i에서, 
V - Y 까지, 최소 거리를 의미한다.

만약, 이미 Y에 속한 노드들이라면
-1 로 표기해준다.


'''
def prim(W):
    # 초기화 작업
    n = len(W) - 1
    F = []
    nearest  = [-1] * ( n + 1 ) # 0번째 idx는 비어있는 상태로 작업
    distance = [-1] * ( n + 1 ) 

    # i에는 1이라는 노드를 선택.
    # 1 이라는 노드를 시작점으로 하여, 출발할 것이다.
    # distance[i] 란, 1노드에서 각 노드까지의 거리
    for i in range( 2, n + 1 ):
        nearest[i] = 1
        distance[i] = W[1][i] 


    for _ in range(n-1): # n-1개의 edge가 선택될 때까지 반복
        minVal = INF
        for i in range( 2 , n + 1 ) :
            '''
            Y에 선택되지 않은 노드 중에서,
            Y 집단에 가장 가까운 거리에 있는 노드를 선택하는 과정
            '''
            if( 0 <= distance[i] and distance[i] < minValue ):
                minValue = distance[i]
                vnear = i # vnear에는 우리가 선택한 노드가 들어간다

            # vnear 는 우리가 방금 선택한 노드
            # nearest[vnear] : 사실상 이전에 선택했던 노드
            # W[nearest[vnear]][vnear] : 2개 노드의 거리
            # 이것을 tuple 형식으로 만들어준다.
            edge = ( nearest[vnear] , vnear, W[nearest[vnear][vnear]] ) 

            F.append(edge) # F에는, 우리가 프림 알고리즘 진행 과정에서 선택한 엣지들이 들어간다.
            distance[vnear] = -1

            # 자. 이제 다시 distance[i] 값들을 update 시켜주어야 한다.
            # distance[i] 는 사실 prim 알고리즘 상, key값에 해당한다
            # 다시 말해서, Y 에 속한 노드들까지의 최소거리가 저장되는데
            # 우리는 vnear라는 노드를 새롭게 Y에 추가했기 때문에
            # distance 값들을 update 시켜주어야 한다는 것이다
            for i in range( 2,  n + 1 ) :
                if( distance[i] > W[i][vnear] ) :
                    distance[i] = W[i][vnear]
                    nearest[i] = vnear
    return F

def cost(F) :
    total = 0
    for e in F :
        total += e[2]
    return total

def print_nd( F , nearest, distance ) :
    print('F = ', end = '')
    print(F)
    print('nearest   ' , end = '')
    print(nearest)
    print('distance  ' , end = '')
    print(distance)

# -------------------------------------------
INF = 999
# 0번째 col, row는 쓰이지 않는다
W = [
    [-1,-1,-1,-1],
    [-1, 0, 2, 3],
    [-1, 5, 4, 3],
    [-1, 6, 2, 3]
]

F = prim(W)
for i in range(len(F)) :
    print(F[i])

print("Minimum Cost is ", cost(F,W))