class Node :
    def __init__(self, item ):
        self.val = item
        self.left = self.right = None

class BinarySearchTree :
    def __init__(self, item) :
        self.head = Node(None)

        self.preorder_list = []
        self.inorder_list  = []
        self.postorder_list = []

    # 전위 순회 : 자기 + 왼쪽 + 오른쪽 
    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)
        
    def __preorder(self,cur):
        self.preorder_list.append(cur.val)
        print(cur.val)
        if cur.left is not None :
            self.__preorder(cur.left)
        if cur.right is not None :
            self.__preorder(cur.right)
    
    # 중위순회 : 왼쪽 , 자기, 오른쪽 
    def inorder_traverse(self) :
        if self.head is not None :
            self.__inorder(self.head)
    
    def __inorder(self, cur) :
        if cur.left is not None:
            self.__inorder(cur.left)
        self.inorder_list.append(cur.val)
        print(cur.val)

        if cur.right is not None :
            self.__inorder(cur.right)

    # 후위 순회 : 왼쪽, 오른쪽 , 자기
    def postrder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)
    
    def __postorder(self, cur ) :
        if cur.left is not None :
            self.__postorder(cur.left)
        if cur.right is not None :
            self.__postorder(cur.right)
        self.postorder_list.append(cur.val)
        print(cur.val)