# https://leetcode.com/problems/maximum-width-of-binary-tree/

'''
첫번째 풀이 : Time Limit Exceed

원리는 간단했다. 
그냥 모든 트리의 레벨을 다 꽉 채운다음
숫자가 존재하는, 첫, 끝 idx를 구한다음
그 idx끼리의 차이 + 1 
을 해주면 len이 나오므로,

각 레벨에 대해서 idx 차이 + 1을 해준다음
그 중에서의 max 를 구했다

하지만, 레벨에 따라서 무한정 노드가 많아질때, 
ex. 10번 레벨만 내려가도 , 한 레벨에 존재하는 노드의 수는 2 ^  10 개

이것을 다 검사하는 것은 무리가 있다. 


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        res = 1
        
        while queue :
            
            tmp = []
            print("queue", len(queue))
            for q in queue :
                if q != None:
                    tmp.append(q.left)
                    tmp.append(q.right)
                elif q == None:
                    tmp.append(None)
                    tmp.append(None)
            
            queue = tmp
            
            if len(queue) == 0:
                break
            
            minSt = len(queue)
            maxEd = 0
            
            # 여기서부터 값 탐색하기
            for i in range( len(queue) // 2 ) :
                if queue[i] != None and i < minSt :
                    minSt = i
                if queue[ len(queue) - 1 - i ] != None and len(queue) - 1 - i > maxEd :
                    maxEd = len(queue) - 1 - i
            
            # 실제 1보다 길때만 계산하면 된다
            if minSt != len(queue) and maxEd != 0 :
                res = max(res, ( maxEd - minSt ) + 1 )

           
        
        return res
            

'''
두번째 풀이 : None이 아닌 노드에 idx 부여하기
assign position value to each node !!

이진트리에서
루튼노드의 idx를 기준으로
왼쪽 자식 노드의 idx는 2 * idx
오른쪽 자식 노드의 idx는 2 * idx + 1

즉, 모든 레벨에서, 모든 노드를 검사하는 것이 아니라,
왼쪽 끝, 오른쪽 끝 노드끼리의 idx 차이 + 1 을 해주면서
그 중에서 최댓값을 구해나가면 된다
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 1
        queue = deque([(root,0)])
        
        while queue :
            # width 계산
            _ , left  = queue[0]
            _ , right = queue[-1]
            res = max(res, ( right - left ) + 1 )
            # next level 형성하기
            tmp = []
            for q in queue :
                node , idx = q[0], q[1]
                if node.left : tmp.append((node.left, 2 * idx ))
                if node.right : tmp.append((node.right, 2 * idx + 1 ))
            queue = tmp
        
        
        return res
            
                    
            
                
        
        
        
        