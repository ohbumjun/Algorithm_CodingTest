#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int n;
    Node* prev;
    Node* next;
    Node(int n, Node* prev, Node* next) : n(n), prev(prev), next(next){}
};

string solution(int n, int k, vector<string> cmd) {
    string answer (n, 'X');
    
    Node* cursor = new Node(0, NULL, NULL);
    
    // n - 1개 추가 생성
    for (int i = 1; i < n; ++i)
    {
        cursor->next = new Node(i, cursor, NULL);
        cursor = cursor->next;
    }
    
    for (int i = 0; i < n - k - 1; ++i)
    {
        cursor = cursor->prev;
    }
    
    stack<Node*> delStack;
    
    for (const string& str : cmd)
    {
        if (str[0] == 'U' || str[0] == 'D')
        {
            int num = stoi(str.substr(2));
            
            if (str[0] == 'U')
            {
                while (num--)
                    cursor = cursor->prev;
            }
            else 
            {
                while (num--)
                    cursor = cursor->next;
            }
        }
        else if (str[0] == 'C')
        {
            delStack.push(cursor);
            
            // 관계 재설정
            if (cursor->prev != NULL)
                cursor->prev->next = cursor->next;
            if (cursor->next != NULL)
                cursor->next->prev = cursor->prev;
            
            // 자리 옮기기
            if (cursor->next != NULL)
                cursor = cursor->next;
            else 
                cursor = cursor->prev;
        }
        else if (str[0] == 'Z')
        {
            Node* reNode = delStack.top();
            delStack.pop();
            if (reNode->prev != NULL)
                reNode->prev->next = reNode;
            if (reNode->next != NULL)
                reNode->next->prev = reNode;
        }
    }
    
    // String 만들기
    while (cursor->prev)
        cursor = cursor->prev;
    while(cursor)
    {
        answer[cursor->n] = 'O';
        cursor = cursor->next;
    }
    
    return answer;
}