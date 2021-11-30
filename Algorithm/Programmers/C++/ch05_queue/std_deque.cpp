#include <iostream>
#include <deque>

using namespace std;

int main()
{
    deque<int> d {10,20,30,40};

    d.push_front(50);
    d.push_front(60);

    for (int i = 0; i < d.size(); i++)
        cout << d[i] << ", ";
    return 0;
}