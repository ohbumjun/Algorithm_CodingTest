// forward_list : 단순 연결 리스트 --- 
// 순방향 연산 및 이동만 가능하다

// ---------------------------
// begin()
// end()
// before_begin() 

// ---------------------------
// 삽입, 삭제의 경우
// 특정 위치 "다음"에 원소 삽입
// 리스트 맨 앞에 원소 삽입
// insert_after, erase_after, emplace_after
// push_front, emplace_front, pop_front

// std::distance() -- 전체 size 할 수 있따

#include <iostream>
#include <forward_list>

using namespace std;

int main()
{
    forward_list<int> l1 {10,20,30,40};
    l1.push_front(40);
    l1.push_front(30); // 30,40,10,20,30,40

    for(const auto& a : l1)
        cout << a << ". ";

    // 개수
    int cnt = distance(l1.begin(), l1.end());

    // 값을 제거 --> 모든 40이 제거
    l1.remove(40);

    // 조건에 맞는 녀석만 제거
    l1.remove_if([](int n){return n > 20; }) // int 형 자료를 하나 받아서, 20보다 큰 녀석만 해당 원소가 삭제가 될 것이다 
    
    return 0;
}




