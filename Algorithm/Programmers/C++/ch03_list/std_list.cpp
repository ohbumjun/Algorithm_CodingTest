// std::list

#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<int> l1;
    l1.push_back(10);
    l1.push_back(20); // 10,20

    list<int> l2 {10,20,30,40};

    for(const auto& a: l2)
        cout << a << ", ";

    // 첫번째 인자 : 반복자 --> 위치 
    // 두번째 인자 : 다른 list 이름 
    // l1의 요소가 복사가 되는 것이 아니라, 이동
    // 따라서, 이제 l1에는 아무값도 없게 된다. 
    l2.splice(l2.end(), l1); // l2 끝네 l1을 붙인다 --> 10,20,30,40 + 10,20

    l2.sort(); // 정렬

    l2.unique(); // unique 값 
}
