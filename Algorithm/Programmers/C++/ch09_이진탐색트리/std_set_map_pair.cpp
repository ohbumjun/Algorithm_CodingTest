/*
>> set와 map의 차이
- set은 키. 만 저장
- map은, 키, 값.을 저장 

>> set과 multi set
- set은 고유한 키의 데이터만 저장, 중복 허용 x
- multiset은 중복되는 데이터 저장

>> set, unordered_set
- set은 내부에서 데이터 정렬해서 저장
- unordered_set은 데이터 정렬 x
- 정렬 과정으로 unordered_set보다는 느리다

template<
    class Key,                              // Key 카입, 키(key) 값을 저장하는 연관 컨테이너
    class Compare = std::less<Key>,         // 정렬 기준 : 기본 오름차순 
    class Allocator = std::allocator<Key>>  // 내부에서 데이터 저장 위애 메모리 할당 방법 
class set;

- 삽입 , 삭제, 탐색 모두 O (log n) --> 내부적으로 균형이진트리 일정인, 
                                        레드 블랙 트리.를 이용하여 구현되기 때문
- 중복되는 데이터를 set 구조로 저장하려면, std::multiset 컨테이너 사용
- 데이터를 정렬되지 안흔 상태로 저장하려면, std::unordered_set 컨테이너 사용 


- rbegin(), rend() : 순방향 및 역방향 반복자 반환
- 

*/
#include <iostream>
#include <set>

using namespace std;

int main()
{
    set<int> odds = {1, 5, 9, 3, 7}; // 오름차순 형태로 저장되어 있을 것이다
    set<int, greater<>> evens = {2, 4, 6, 8}; // 내림 차순 정렬
    set<pair<string,int>> managers = {{"b",1}, {"a",3}, {"c",2}}; // 문자열, 정수값 쌍을 저장
    managers.insert(make_pair("d",4));
    managers.insert({"e",6});

    // pair의 경우, 먼저 string 기준 정렬 --> 같은 string이면, int 를 이용하여 오름차순 정렬 
    // 즉, 크기비교를 자동으로 수행해준다. 
    using psi = pair<string,int>;
    set<psi> managers2;

    struct psi2
    {
        string first;
        int second;
    };

    // 오류가 난다. 왜냐하면, psi2 는 자체 정렬 기능이 없기 때문이다.
    // 즉, 사용자 정의 type읆 만들어서 set에 저장하고 싶다면
    // 사용자 정의 type 에 대해서 크기 비교가 가능하도록
    // 부등호 연산자 오버로딩을 해야 한다. 
    set<psi2> managers3; 
    

    for (const int &o : odds)
        cout << o << ", ";
    
    evens.insert(10); // 제일 앞에 위치할 것이다
    evens.insert(2);  // 중복된 값 insert --> 무시된다. 

    for(const n : evens)
        cout << n << ", ";
    
    if(evens.find(4) != evens.end()) // 찾으면, 해당 위치 반복자 반환 , 아니면 end() 반환
        cout << "4 is found" << endl;
    
    psi person1 = {"a",3};
    if(managers.find(person1) != managers.end())
        cout << "person1 not found" << endl;
    
    managers.erase({"e",5});

    return 0;
}