#include <iostream>
#include <array>

// 단점 
// - 항상 배열 원소를 스택 메모리를 사용 --> 대용량 저장시 스택 오버 플로우 
// - 고정 크기 배열 only --> 가변 크기 배열 지원 x 
// - 대신 std::vector를 더 활용 

using namespace std;

int main()
{
    array<int, 5> scores = {4, 5, 6, 7, 8};
    int s = 0;
    for (int i = 0; i < scores.size(); i++)
    {
        s += scores[i];
    }
    return 0;
}