// 배열 또는 stl 컨테이너에 들어있는 모든 원소를 순차적으로 접근하는 c+11 의 새로운 반복문
#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    vector<int> numbers {10,20,30};
    string strs[] = {"I", "love", "you"};
    

    // &을 안쓸 수도 있다. --> 복사해서 가져오는 형태
    for (int n : numbers) 
        cout << n << endl;

    // &을 써서, 참조 형태로 받아올 수 있다. --> 복사 x, 위의 10,20,30을 참조형태로 받는 것 
    // 여기서 n값을 변경하면, 실제 numbers 안의 값도 변경이 된다. 
    for (auto& n : numbers)
        cout << n << endl;

    // 아래와 같은 코드
    for (auto iter = begin(numbers); iter < end(numbers); ++iter)
    {
        cout << *iter << endl;
    }

    // 참조로 받아오기 + const를 통해 바꾸지 않을 것임을 병시 
    for (const auto& s :strs)
        cout << s << " ";
    return 0;
}

