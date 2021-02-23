# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int :
        
        '''
        dp 문제이다.
        dp에서의 핵심은, 가장 작은 단위를 무엇으로 잡을 것이냐이다 .
        
        가장 작은 단위의 input은 root만 들어올때
        즉, 원소의 개수가 1개일 때 !
        
        10
        4
        1 5 
        
        이렇게 있을 경우 : 16 
        
        10
        20
        1 5 
        
        이렇게 있을 경우 : 20
        
        다른 예시를 들어보자
        3
        4    5
        1 3  1
        
        4
        1 3 
        에 대한 subtree에 대해서 우리가 계산하여 얻는 값은
        [ 4, 4 ]
        
        5
        1
        에 대한 subtree 에 대해서 우리가 계산하여 얻는 값은
        [ 5, 1 ]
        
        그렇다면 
        3
        이라는 루트노드에 대한 계산으로
        우리는 어떤 값을 얻게 될까?
        [ 8, 9 ] ! 
        
        1) 해당 노드를 선택할 경우 : 자식 노드를 선택하지 못함
        = 해당 노드 + 자식,자식 노드들의 합
        8 = 3 + ( ( 1 + 3 ) + 1 ) 
        
        2) 해당 노드를 선택하지 않는 경우 : 자식 노드들, 
        구체적으로는 자식 subtree 들 경우의 수중 최대값 
        
        9 = 4 + 5
        
        ------------------------------------------------------ 
        < 아래와 같이 로직을 생각할 수 있다 >
        
        1) 해당 노드 선택할 때 :
        해당 노드값 + 왼쪽 손자 서브트리에서의 최대값 + 오른쪽 손자 서브트리에서의 최대값 
        
        2) 해당 노드 선택안할 때 :
        (왼쪽 자식 포함) 왼쪽 자식 서브 트리에서의 최대값 + (오른쪽 자식 포함) 오른쪽 서브 트리에서의 최대값  
        
        
        '''

        def decision(node) :
            
            if node == None :
                return [0,0]
            
            # 전위 순회 : 왼쪽 + 오른쪽
            # 그 이후 return 값들로 계산
            [leftRob, leftNotRob]  = decision(node.left)
            [rightRob,rightNotRob] = decision(node.right)
            
            robNodeVal    = node.val + leftNotRob + rightNotRob
            robNotNodeVal = max(leftRob + rightRob , leftRob + rightNotRob , leftNotRob + rightRob, leftNotRob + rightNotRob )
            
            return [robNodeVal, robNotNodeVal]
        
        return max(decision(root))
        
            
                
                