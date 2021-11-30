//std::stack
/*
template<class T, class Container = std::deque<T>>
class stack;

Contaier는 내부에서 사용할 컨테이너를 지정
deque, vector, list를 지정할 수 있다

기본 deque를 보통 사용
*/

#include <iostream>
#include <stack>

using namespace std;

int main()
{
    std::stack<int> stk;
    stk.push(10);
    stk.push(20);
    stk.push(30);
    stk.pop();

    cout << stk.top() << endl;

    while(!stk.empty())
    {
        auto& e = stk.top();
        cout << e << ", ";
        stk.pop();
    }
}