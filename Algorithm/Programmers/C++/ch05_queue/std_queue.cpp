/*
template<class T, class Container = std::deque<T>>
class queue;
*/

#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);
    q.pop();

    cout << q.front() << endl;

    while (!q.empty())
    {
        int& e = q.front();
        cout << e << " ,";
        q.pop();
    }
    return 0;
}