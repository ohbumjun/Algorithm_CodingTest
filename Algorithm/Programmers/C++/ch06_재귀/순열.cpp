// 모든 순열 출력하기
// 1. 첫번째 원소를 모든 원소와 맞바꾸기
// - 다른 원소들이 각각 맨 처음 위치로 올 수 있도록 swap 하는 것

// 2. 첫 원소 제외한 나머지 원소들의 집합으로, 재귀적으로 순열 구하기 호출 

#include <iostream>
#include <vector>

using namespace std;

void permutation(vector<int>& vec, int k)
{
    if (k == vec.size() -1)
    {
        for (const auto& v : vec) 
            cout << v << ", ";
        return;
    }

    for (int i = k; i < vec.size(); i++)
    {
        // swap
        int temp = vec[i];
        vec[i] = vec[k];
        vec[k] = temp;

        permutation(vec,k+1);

        // 순서 원복 
        int temp = vec[i];
        vec[i] = vec[k];
        vec[k] = temp;
    }
};



int main()
{
    return 0;
}