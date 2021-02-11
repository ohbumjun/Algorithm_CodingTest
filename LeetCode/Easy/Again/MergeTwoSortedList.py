# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
				# 빈 배열을 선언한다 
        array = list()
        
        # l1의 val을 모두 array에 넣는다
        while( l1 != None):
            array.append(l1.val)
            l1 = l1.next
        
        # l2의 val을 모두 array에 넣는다
        while( l2 != None):
            array.append(l2.val)
            l2 = l2.next
            
        array = sorted(array)
        mergedlist = None
        
        for i in range(len(array)):
            if i == 0 :
                mergedlist = ListNode(array[i]) # val을 넣기만, 하면, 생성자에 의해, 바로 해당 노드가 만들어진다 
            else:
                new_node   = ListNode(array[i])
                cur_node   = mergedlist # C언어로 따지면, head 에 대한 정보를 넣는 것이다.
                while cur_node.next != None:
                    cur_node = cur_node.next
                cur_node.next = new_node
                
                
        return mergedlist