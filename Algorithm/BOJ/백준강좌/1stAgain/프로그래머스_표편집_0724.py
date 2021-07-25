# https://programmers.co.kr/learn/courses/30/lessons/81303

# 삽입 삭제가 빈번하게 이루어지는 문제의 경우
# map같은 자료구조는 쉽게 시간초과가 발생하게 된다
# hash map 혹은 양방향 연결리스트를 통해
# 문제를 풀어야 한다

# 양방향 연결리스트 활용하기
def from os import link


Node:
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

# ------------------------------------------------------
# 실제 풀이


def up(cur, i, link_info):
    """ 
    명령어 'U i' 를 동작하는 함수 
    cur : 현재 위치
    i : 반복할 횟수
    link_info : 연결관계를 저장함 link_info[node] :[이전 노드의 번호, 다음 노드의 번호]
    """
    for _ in range(i):
        pre, post = link_info[cur]
        cur = pre
    return cur


def down(cur, i, link_info):
    """
    명령어 'D i' 를 동작하는 함수
    cur : 현재 위치
    i : 반복할 횟수
    link_info : 연결관계를 저장함 link_info[node] :[이전 노드의 번호, 다음 노드의 번호]
    """
    for _ in range(i):
        pre, post = link_info[cur]
        cur = post
    return cur


def recover(status, trash, link_info):
    """
    명령어 Z를 수행하는 함수
    cur : 현재 위치
    status[i] : i번쨰 원소가 삭제 여부를 저장하는 함수 존재하면 1 삭제면 0
    trash : 삭제된 노드와 연결정보를 저장 / trash[node] : [이전 노드의 번호, 다음 노드의 번호]
    link_info : 연결관계를 저장함 / link_info[node] :[이전 노드의 번호, 다음 노드의 번호]
    """

    # 가장 최근에 삭제된 원소를 불러온다.
    # .popitem() : 가장 마지막에 삽입된 item을 가져온다
    deleted, node_info = trash.popitem()

    # 존재여부를 업데이트 시켜주고
    status[deleted] = 1  # 삭제x, 존재
    pre, post = node_info  # [pre,post]

    # 연결 정보를 업데이트 해준다.
    link_info[deleted] = [pre, post]  # --> 연결리스트 중간에 넣기만 !

    # 이후, 연결리스트 넣은 위치, 앞,뒤와 관계를 재설정
    # A-C-D --> A,B,C-D --> A-B-C-D
    # 이전 노드의 연결정보 업데이트 만약 None이라면 복원된 노드가 맨 앞의 원소이므로 업데이트 X
    if pre != None:  # pre == None : pre x --> 우리가 삽입한 노드 앞과의 연결관계를 설정할 필요 x
        link_info[pre][1] = deleted

    # 이후 노드의 연결정보 업데이트 만약 None이라면 복원된 노드가 맨 뒤의 원소이므로 업데이트 X
    if post != None:  # post == None : 우리가 삽입한 노드가 맨 마지막 ! 뒤와의 연결관계를 설정할 필요 x
        link_info[post][0] = deleted

    return


def delete(cur, status, trash, link_info):
    """
    명령어 C 를 수행하는 함수
    cur : 현재 위치
    status[i] : i번쨰 원소가 삭제 여부를 저장하는 함수 존재하면 1 삭제면 0
    trash : 삭제된 노드와 연결정보를 저장 / trash[node] : [이전 노드의 번호, 다음 노드의 번호]
    link_info : 연결관계를 저장함 / link_info[node] :[이전 노드의 번호, 다음 노드의 번호]
    """

    # 현재 위치 삭제
    status[cur] = 0  # 0: 삭제!

    # 쓰레기통에 삭제한 정보를 넣어 준다.
    pre, post = link_info[cur]
    trash[cur] = link_info.pop(cur)

    # 만약 삭제된 노드가 마지막 노드였다면
    if post == None:
        # 삭제된 노드의 이전 노드가 마지막 노드로 업데이트
        link_info[pre][1] = None
        return pre
    # 만약 삭제된 노드가 첫번쨰 노드였다면
    elif pre == None:
        # 삭제된 노드의 다음 노드가 첫번째 노드로 업데이트
        link_info[post][0] = None
    else:  # 중간에 있는 노드라면
        # 이전 노드와 다음 노드를 연결해준다.
        link_info[post][0] = pre
        link_info[pre][1] = post
    return post


def solution(n, k, cmd):

    answer = ''
    status = [1 for i in range(n)]
    trash = {}
    link_info = {i: [i-1, i+1] for i in range(1, n-1)}
    link_info[0] = [None, 1]
    link_info[n-1] = [n-2, None]

    # 커맨드에 따라 동작
    for c in cmd:
        command = c[0]
        if command == "U":
            i = int(c.split()[-1])
            k = up(k, i, link_info)
        elif command == "D":
            i = int(c.split()[-1])
            k = down(k, i, link_info)
        elif command == "C":
            k = delete(k, status, trash, link_info)
        else:
            recover(k, status, trash, link_info)

    # 존재 여부를 이용해 답을 작성한다.
    answer = ''.join(['O' if i else 'X' for i in status])
    return answer
