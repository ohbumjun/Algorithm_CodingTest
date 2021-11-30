// (단순) 연결 리스트란 ? --- 
// 데이터. 링크. 로 구성된 노드. 가 연결되어 있는 자료구조
// 데이터 :
// 링크 : 다음 노드를 가리키는 포인터
// 데이터, 링크.로 이루어진 연결리스트 구성 단위

struct Node
{
    int Data;
    Node* Next;
};

// (이중) 연결리스트 --- 
// 이전 노드와, 다음 노드에 대한 링크를 가지고 있는 연결리스트
// 더미노드 : Header, Tail
// - 특정 값을 가진 노드가 아니라, 전체 이중 연결리스트 관리를 위해 추가한 노드
struct Node 
{
    int data;
    Node* prev;
    Node* next;
};

class DoublyLinkedList
{
private :
    int count;
    Node* head;
    Node* tail;
public :
    void insert(Node* p, int val);
    void erase(Node* p);
    void print_all();
    void print_reverse();
};

// (원형) 연결리스트 ---
// 연결 리스트 마지막 노드링크가, 처음 노드 가리키도록 

