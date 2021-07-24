# https://programmers.co.kr/learn/courses/30/lessons/81303

# 삽입 삭제가 빈번하게 이루어지는 문제의 경우
# map같은 자료구조는 쉽게 시간초과가 발생하게 된다
# hash map 혹은 양방향 연결리스트를 통해
# 문제를 풀어야 한다


# 양방향 연결리스트 활용하기
def Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        se.f.next = next


class DoubleLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data, prev=node)
            node.next = new
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    # 중간, 특정 값 이전에 값을 insert 하기

    def insert_before(self, next_data, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
            return True
        else:
            node = self.tail
            while node.data != next_data:
                node = node.prev
            prev_node = node.prev
            new_node = Node(new_data, prev=prev_node, next=node)
            if prev_node:
                prev_node.next = new_node
            else:
                self.head = new_node
            node.prev = new_node
            return True
    # 중간, 특정 값 다음에 값을 insert 하기

    def insert_after(self, before_data, new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
            return True
        else:
            node = self.head
            while node.data != before_data:
                node = node.next
                if node == None:
                    return False
            next_node = node.next
            new_node = Node(new_data, prev=node, next=next_node)
            if next_node:
                next_node.prev = new_node
            else:
                self.tail = new_node
            node.next = new_node

    def solution(n, k, cmd):
