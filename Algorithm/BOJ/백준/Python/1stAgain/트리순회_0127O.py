import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(10000)

class Node:
    def __init__( self, val, left, right ) :
        self.val   = val
        self.left  = left
        self.right = right

def preorder(node): # 전위순회 : 자기 + 왼쪽 + 오른쪽
    print(node.val , end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node) : # 중위 순회 : 왼쪽 + 자기 + 오른쪽
    if node.left != '.':
        inorder(tree[node.left])
    print(node.val, end = '')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node) : # 후위 순회 : 왼쪽 + 오른쪽 + 자기
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.val, end = '')

if __name__ == "__main__":
    n = int(input())
    tree = {}

    for _ in range(n) :
        root, left, right = map(str,input().split())
        tree[root] = Node(root,left,right)
   
    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
    print()
'''
tree 라는 dict를 두고
key값이 곧, 특정 노드
그리고 그 key에 대한 value로 특정 노드가 들어가며
그 특정 노드 안에는 3가지 값이 들어있다
1) val, 2) left, 3) right
'''