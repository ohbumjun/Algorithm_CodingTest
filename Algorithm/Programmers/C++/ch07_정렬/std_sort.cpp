#include <iostream>
#include <algorithm>
#include <vector>

/*
template<class RandomIt>
void sort(RandomIt first, RandomIt last); // 반복자 2개 받기 

template<class RandomIt, class Compare>
void sort(RandomIt first, RandomIt last, Compare comp); // 반복자 2개 + 함수 객체 받기

기본값 : 오름차순 정렬 
vector, deque, array 등 정렬시 사용

list, forward_list는 자체의 sort() 함수 사용
*/

using namespace std;

// 함수 포인터
bool abs_cmp(const int a, const int b)
{
    return std::abs(a) < std::abs(b);
};

// 함수 객체 
struct AbsCmp 
{
    bool operator() (int a, int b) const
    {
        return std::abs(a) < std::abs(b);
    } 
};

class Person
{
public :
    string name;
    int age;

    bool operator < (const Person& a) const 
    {
        return this->age < a.age;
    }
};


int main()
{
    int arr[5] = {4, 2, 5, 3, 8};
    sort(arr, arr+5);
    sort(begin(arr), end(arr));
    sort(begin(arr), end(arr), greater<>()); // 내림 차순 --> greater 라는 함수 객체를 전달하는 형태가 된다 
    sort(begin(arr), end(arr), less<>());    // 오름 차순 --> default : less<>() 

    vector<string> vec = {"orange", "banana", "apple", "lemon"};
    sort(vec.begin(), vec.end());
    sort(vec.begin(), vec.end(), greater<>()); // 내림차순

    // 함수 포인터를 사용하여, 비교 방법 지정하기 
    vector<int> nums = {10,2,-3,5,7};
    sort(nums.begin(), nums.end(), abs_cmp); // 절대값 기준 , 오름차순 정렬 

    // 함수 객체 사용하기 (function object, functor)
    sort(nums.begin(), nums.end(), AbsCmp()); // 절대값 기준 , 오름차순 정렬 

    // 람다 표현식
    sort(nums.begin(), nums.end(), [](int a, int b){
        return std::abs(a) < std::abs(b);
    }); 

    // 비교 연산자 오버로딩한 객체의 정렬 
    vector<Person> v;
    v.push_back({"A",10});
    v.push_back({"C",20});
    v.push_back({"B",30});

    return 0;
}