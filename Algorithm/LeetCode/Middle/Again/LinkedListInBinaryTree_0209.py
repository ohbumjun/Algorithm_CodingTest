# https://leetcode.com/problems/linked-list-in-binary-tree/
'''
우선적으로 고려해야 하는 것이 있다.

ListNode 안에서, 맨첫번째 요소는 반드시 TreeNode 에 있어야 한다.
그렇다면,

1) 
TreeNode 의 수많은 value 중에서
ListNode의 첫번째 value인 애들을 담는다.

2)
담은 애들을 시작점으로 하여,
path를 검사하여,
그 중 하나라도 path가 존재한다면, 최종결과 return true

3) 
path를 검사할때, 왼쪽, 오른쪽으로 가면서 재귀적으로 검사한다.
두 path에서 하나라도 존재한다면 그것은 true로 인식된다. 

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.startNodes = []
        
    def checkHead (self, head , root ) :
        if head == None: return
        if root == None : return
        
        if head.val == root.val :
            self.startNodes.append(root)
            
        self.checkHead(head , root.left)
        self.checkHead(head, root.right)
    
    def checkPath(self,head,root) :
        if head == None : return True # 모두 검사했다는 의미 
        if root == None : return False 
        
        if head.val == root.val :
            checkLeft  = self.checkPath( head.next, root.left )
            checkRight = self.checkPath( head.next, root.right )
            if checkLeft == True or checkRight == True :
                return True
        return False

    def isSubPath(self, head, root):  
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        self.checkHead(head,root)
        for Node in self.startNodes :
            tmp = self.checkPath(head, Node)
            if tmp :
                return True
            