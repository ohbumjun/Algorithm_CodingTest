# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self) :
        self.result = -1001
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findMaxSum(root)
        return self.result
    
    def findMaxSum(self, root) :
        
        # 1. path may start & end, at any part of tree, but should always be continuous
        # 2. path may not be going through the root
        # 3. path can have one node minimum
        
        # 3 cases for each node
        # Case 1.
        # current node is in the path of max sum
        # ms = max( ( left , right ) + root , root  )
        
        '''
        why ? max(left, right) ?
        
        if we consider Case1 , 
        it means that, path is coming from 
        either left, or , right
        
        which means that, both left, right paths are 
        not considered in 'Case 1'
        '''
        
        # Case 2.
        # current node is the root , for max sum path
        # m2s = max( ms , left + right + root )
        '''
        if current Node is the 'root', 
        then left, right path sum should be included
        
        but also, we are comparing with Case 1.
        '''
        
        # Case 3.
        # current node is not included in max sum path
        # result = max( m21, result )
        '''
        In the very beginning, 
        we are considereing from the leaf node.
        which means that
        we se 'leaf node' result as 'INT_MIN'
        
        since, current 'leaf node' is not included in 'max-sum' path ,
        there might be 'max sum' somewhere in the tree
        and !
        since we are finding the 'maximum',
        we set result as 'Int_Min'
        and then 
        
        compare with Case 2
        '''
        
        # How to Solve
        # default : preorder_traversal !
        # 1) we need to maintain a variable to keep track of max sum already found ( for Case 3 )
        # 2) we need to compare all 3 cases for each node
        
        '''
        Additional Consideration 
        - what should we return from the function ??
        - we are considering from the 'leaf-node' , which means that
        - we are applying recursive function, and comming up from the bottom
        - so we have to return certain value in each recursvie function 
        - so that upper recursive function can make usage of that 
        
        BUT !! 
        in Case2, Case 3, 
        we return nothing !
        
        why ? 
        > in terms of Case2 ,
        current Node is the root !
        there can be no Node that is located above the current Node,
        that is why we return nothing from the current recursvie func to upper recursive func
        
        > in terms of Case3 ,
        current Node is not included in max sum path,
        any value got in Case 3, 
        is not considered in upper recursive func ! 
        '''
        
        
        if root == None :
            return 0
        
        left  = self.findMaxSum( root.left  )
        right = self.findMaxSum( root.right )
        
        # case1
        Case1 = max ( max(left, right) + root.val , root.val )
        # case2
        Case2 = max( Case1 , left + right + root.val )
        # case3
        self.result = max( self.result , Case2 )
        
        return Case1
        
        