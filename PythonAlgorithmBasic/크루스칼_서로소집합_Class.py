# 서로소 집합 Disjoint Set : Union-Find

class DisjointSet :
    def __init__( self, n ) : # n : n개의 노드
        self.U = [] # 부모 집합
        for i in range(n) :
            # 자기 자신을 부모로서 갖게 한다.
            self.U.append(i)
        
    # 부모 찾는 함수
    def find (self, i ) :
        j = i 
        while(self.U[j] != j) :
            # 자기자신의 부모가, 자기 자신을 가리킬 때까지
            # 밑에서부터 위로 올라가는 것이다.
            j = self.U[j]
        return j  

    def union( self, p , q ) :
        if( p < q ) :
            self.U[q] = p
        else :
            self.U[p] = q 

    # find 함수를 통해 p, q 에 대한 대표선수를 반환 받으면
    # 즉, 각 노드의 루트노드를 반환받으면
    # 비교하여 setting 하는 것이다. 
    def equal( self, p, q) :
        if( p == q ):
            return True
        else:
            return False

# 크루스칼 알고리즘
def kruskal( n , E ) : # E : 가중치 순서대로 string된 상태여야 한다.
    F = [] 
    dset = DisjointSet(n) # n만큼 disjoint set을 만든다. n은 정점 집합의 크기
    while( len(F) < n - 1 ) : # F의 size가 n-1이 될때까지. ( edge의 개수 )
        edge = E.pop(0) # 앞의 것을 뽑는다
        i , j = edge[0] , edge[1]
        p = dset.find(i) # 루트 노드, 즉 집합을 찾는다
        q = dset.find(i)

        # 사이클을 형성하지 않는다면
        if( not dset.equal(p , q )) : # 집합이 서로 다르다면 
            dset.union( p , q ) # 집합을 합친다.
            F.append(edge) 
            print("accedpted", edge)
        # 버려진 것 확인하기
        else:
            print("discarded", edge)
    return F

# 결과적으로 F에 있는 edge의 가중치 값들을 다 더하면 그것이 답이 된다. 