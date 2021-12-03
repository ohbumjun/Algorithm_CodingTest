/*
template<
    class Key,                              // Key 카입, 키(key) 값을 저장하는 연관 컨테이너
    class Compare = std::less<Key>,         // 정렬 기준 : 기본 오름차순 
    class Allocator = std::allocator<Key>>  // 내부에서 데이터 저장 위애 메모리 할당 방법 
class set;

- Key 타입의 key와 T 타입의 value, 쌍 pair 을 저장하는 연관 컨테이너 
- 데이터 삽입, 삭제는 O(log n)
- set과 마찬가지로, 레드-블랙 트리.를 이용하여 구현된다.
- 중복되는 데이터를 map 구조로 저장하려면, std::multimap 컨테이너 사용
- 데이터를 정렬되지 않은 상태로 저장하려면, std::unordered_map 컨테이너 사용 
- 사용자 정의 타입을 저장하는 경우, 비교 연산을 지원해야 한다. 
- operator [] : 특정 키에 해당하는 원소의 값을, "참조"로 반환
              : 해당 키의 원소가 없으면, 새로운 원소를 기본값으로 생성하여, 참조를 반환 
//
*/

#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<string, int> fruits;
    fruits.insert({"banana", 1500});
    fruits.insert({"apple", 1000}); 
    // apple을 나중에 입력한다고 할지라도, 내부에서 정렬처리 발생
    // 따라서 apple 이 banana 보다 먼저 위치한 형태로 저장될 것이다. 

    fruits.insert(make_pair("orange", 2000));

    for (const auto& a : fruits)
        cout << a.first << " is " << a.second << " won." << endl;
    
    fruits["apple"] = 2000;
    fruits.erase("orange");

    for(auto [name, price] : fruits)
        cout << name << " is " << price << " won." << endl;

    return 0;
}