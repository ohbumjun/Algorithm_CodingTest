class Node :
    def __init__( self, item ) : 
        self.val = item
        self.left = self.right = None

class BinarySearchTree :
    def __init__( self  ) :
        self.head = None
    def add(self, item) :
        if self.head is None :
            self.head = Node(item)
        else:
            self.__add_val(self.head, item)
    def __add_val(self, cur, item ):
        if cur.val >= item :
            # 왼쪽으로 보내야 한다
            if cur.left is not None:
                self.__add_val(cur.left, item)
            else:
                cur.left = Node(item)
        else :
            # 오른쪽으로 보내야 한다.
            if cur.right is not None :
                self.__add_val(cur.right, item)
            else:
                cur.right = Node(item)
    
    def search( self, item ) :
        if self.head.val is None :
            return False
        else:
            return self.__search_node(self.head, item)
    
    def __search_node(self, cur, item) :
        # cur.val은 존재한다는 가정하에 이 함수가 실행된다.
        if cur.val == item :
            return True
        else:
            if cur.val >= item :
                if cur.left is not None :
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None :
                    return self.__search_node(cur.right, item)
                else:
                    return False
    
    '''
    삭제의 원리
    1) 자식 노드가 없을 때
    - 그냥 지우면 된다
    2) 자식 노드가 한개 있을 때
    - 할아버지 노드와, 자식 노드를 지워주면 된다.
    3) 자식 노드가 2개 이상일때
    - 오른쪽 서브 트리, 제일 왼쪽 노드를, 현재 위치에 갖다 놓는다.
    '''

    def delete(self, item ) :
        # root : 삭제 이후 바뀐 루트의 주소
        # self.root 는 곧, 해당 이진트리의 정보이기도 한다
        # deleted : 삭제 여부
        self.root, deleted = self.__delete_val(self.root, item)
        return deleted
    
    def __delete_val(self, node, data) :
        # 아예 해당 노드가 존재하지 않는다면, false를 return한다.
        if node is None:
            return node, False

        # Flag 선언
        deleted = False

        # node.data와 data값이 같으면 데이터 삭제
        if data == node.val :
            # flag 수정 
            deleted = True

            # 2개의 자식 노드가 존재할 경우 
            if node.left and node.right :
                # 해당 노드와 자식 노드를 받는다
                parent, child = node, node.right
                '''
                이게 무슨 말이냐면,
                처음에 현재 node > parent
                현재 node 오른쪽  > child

                이렇게 쭉 따라 내려갔을 텐데,
                만약 하나도 안내려갔다면,
                
                즉, 애초부터, 오른쪽 서브트리의 왼쪽 자식 값이라는 것이 존재하지 않았다면
                parent == node
                이고
                child = node.right 으로 고정이겠지
                '''

                # 오른쪽 자식노드의 left 자식 노드를 탐색하여 가장 작은 값을 가져온다
                while child.left is not None :
                    # 결국 child에, 오른쪽 서브트리, 가장 왼쪽 값이 저장될 것이다.
                    parent, child = child, child.left
                
                # 오른쪽 서브 트리, 가장 왼쪽의 값을 node 위치로 옮기게 되면
                # 옮겨진 노드의 왼쪽은, 기존 node의 left가 된다.
                # chlid가 , 하나도 안내려가고 node.right 인 상태라면
                # node.right , 즉, 오른쪽 노드를, 현재 자리에 그냥 한번 올린다고 생각하면 된다.
                child.left = node.left

                # 지우려는 노드가, 오른쪽 자식 노드를 가지고 있었을 때 
                '''
                parent 가 node가 아니라는 것은
                우선 한번이라도 오른쪽 서브트리에서
                왼쪽 자식 노드로 파고 들어갔다는 얘기.

                그렇다면, 현재 우리가 찾은, 오른쪽 sub tree에서
                가장 왼쪽값이 , 자신의 오른쪽 자식 노드를 가지고 있을 수 있으므로
                가장 왼쪽 노드의 부모 노드에다가
                가장 왼쪽 노드의 자식 노드를,
                자식 노드로 붙여주는 것이다.

                그렇다면 parent == node인 경우에는 왜 이런 작업이 필요 없는 것일까?
                왜냐하면, 어차피 자식 노드가 없다면 
                child, 즉, child.right도 null인 상태. 
                그러므로 , 고려할 필요가 없는 것이다. 
                '''
                if parent != node :
                    parent.left = child.right # 부모의 왼쪽 자식으로, 가장 작은 값의 오른쪽 서브트리를 붙이기
                    child.right = node.right # 가장 작은 값의 오른쪽 서브트리로 지우려는 노드의 오른쪽 서브트리 붙이기

                # 지우려는 노드의 자리에 가장 작은 값으로 대체하기
                node = child
            
            # 하나의 자식 노드만 존재하는 경우
            elif node.left or node.right : # 왼쪽, 또는 오른쪽 자식만 존재
                node = node.left or node.right # 그냥, 해당 자식을 위로 한번 올린다
            
            # 자식 노드가 존재하지 않는 경우
            else :
                node = None # 지우려는 노드를 None으로

        # 아직, 지우려는 data를 찾지 못했다면
        # 1) 지우려는 값이, 현재 노드보다 더 작다면
        elif data < node.val  :
            # 왼쪽으로 이동한다
            node.left, deleted = self.__delete_val( node.left, data )
        # 2) 지우려는 값이 현재 노드보다 더 크다면
        else :
            node.right , deleted = self.__delete_val( node.right, key )
        
        return node, deleted



