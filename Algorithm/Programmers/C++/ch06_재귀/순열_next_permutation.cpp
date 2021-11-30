// 모든 순열 출력하기
// 1. 첫번째 원소를 모든 원소와 맞바꾸기
// - 다른 원소들이 각각 맨 처음 위치로 올 수 있도록 swap 하는 것

// 2. 첫 원소 제외한 나머지 원소들의 집합으로, 재귀적으로 순열 구하기 호출

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void permutation(vector<int> &vec, int k)
{
    if (k == vec.size() - 1)
    {
        for (const auto &v : vec)
            cout << v << ", ";
        return;
    }

    for (int i = k; i < vec.size(); i++)
    {
        // swap
        int temp = vec[i];
        vec[i] = vec[k];
        vec[k] = temp;

        permutation(vec, k + 1);

        // 순서 원복
        temp = vec[i];
        vec[i] = vec[k];
        vec[k] = temp;
    }
};

/*
C++ 함수
- 주어진 시퀀스를 사전순으로 다음에 나오는 순열로 반환
- 정렬된 시퀀스를 호출하기 시작해야함 ( 즉, 호출 전 오름차순 정렬을 수행해야 함 )

std::vector<int> vec{2, 4, 1, 3};
std::sort(vec.begin(),vec.end());

do{
    for(int a : vec)   
        cout << a;
    cout << endl;
}while(std::next_permutation(vec.begin().vec.end()))

*/

int main()
{
    vector<int> vec{1, 2, 3, 4};
    permutation(vec,0);

    sort(vec.begin(),vec.end());

    do{
        for(const int& e : vec)
            cout << e << ". "; 
    }while(std::next_permutation(vec.begin(),vec.end()));
    return 0;
}