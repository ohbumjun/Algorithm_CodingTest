'''
서로소 집합 자료구조.

서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조.

2종류의 연산을 지원
1) 합집합(Union) : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
2) 찾기(Find) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

합치기 찾기(Union Find) 자료구조. 라고도 한다.
'''

# 기본적인 구현 방법 -----------------------------------------------------------
# 특정 원소가 속한 집합 찾기
def find_parent( parent, x ) :
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x :
        return find_parent(parent, parent[x])

# 두 원소가 속한 집합을 합치기
def union_parent( parent, a, b ):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b 

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v, e = map(int,input().split())
parent = [0] * ( v + 1 )  # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range( i , v + 1 ):
    parent[i]  = i

#  Union 연산을 각각 수행
for i in range(e):
    a, b = map(int , input().split())
    union_parent(parent, a ,b)

# 각 원소가 속한 집합 출력하기
print("각 원소가 속한 집합 : ", end = ' ')
for i in range( 1, v + 1) :
    print(find_parent(parent, i) , end = ' ')
print()

# 부모 테이블 내용 출력하기
print("부모 테이블" , end = ' ')
for i in range( 1, v + 1 ) :
    print(parent[i] , end = ' ')


# 기본적인 구현방법을 구현할 때 
# 최악의 경우, 트리형태로 쭉 이어져서, 시간 복잡도가 O ( 노드 개수) 가 될 수 있다 

# 2. 경로 압축 방법 ----------------------------------------------------------
# 찾기 함수(Find)를 재귀적으로 호출한 뒤에, 부모 테이블 값을 바로 갱신한다.
def find_parent( parent, x ) :
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x :
        # 아래의 코드를 통해, 결국 find_parent 함수를 실행하고 나서, 
        # 부모테이블에 적혀있는 부모의 값이, 자신의 루트 노드가 될 수 있도록 해주는 것이다. 
        # find 함수를 호출할 때 사용되었던, 노드에 대한 부모의 값이 루트와 동일하도록, 경로가 압축되는 것
        # 부모테이블의 값에, 반환된 값이 담길 수 있도록 수정하는 것이다.
        parent[x] = find_parent(parent, parent[x])
    return parent[x]