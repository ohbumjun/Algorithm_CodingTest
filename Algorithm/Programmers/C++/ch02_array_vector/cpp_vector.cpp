
// 동적 메모리 할당 ?
// - 프로그램 실행 중 필요한 크기의 메모리 공간을 할당하여 사용하는 기법
// - 사용 끝나면, 명시적으로 메모리 해제
// - C : malloc, calloc 함수로 메모리 할당, free 함수로 메모리 해제
// - C++ : new, delete
// - 힙,메모리 영역을 사용 --> 대용량 배열도 사용 가능

// vector ??
// - 가변 크기 컨테이너

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // 1차원 행렬 ----
    vector<int> v1;
    vector<int> v2(10);    // 10개의 정수 할당하여 사용 --> v2[0] ~ v2[9] 까지 사용 가능, 0으로 초기화
    vector<int> v3(10, 1); // 10개 정수, 1로 초기화
    vector<int> v4{10, 20, 30, 40, 50};
    vector<int> v5 = v4; // 깊은 복사 형태로 생성(복사 생성자)ㅣ
    // vector<int>v5(v4) -- 같은 의미
    vector<int> v6(v4.begin(), v4.begin() + 3); // v4의 맨 처음, 3번째 원소까지로, 초기화

    // 2차원 vector ----
    vector<vector<int>> mat1(2, vector<int>(3));    // 2행 3열 --> 초기값은 0으로 초기화
    vector<vector<int>> mat2(2, vector<int>(3, 1)); // 2행 3열 --> 초기값은 1으로 초기화
    vector<vector<int>> mat3{
        {1, 2, 3},
        {4, 5, 6}
    }; // 2행 3열 --> 초기값은 1으로 초기화

    // v1
    v1.push_back(10);
    v1.push_back(20);

    // mat3
    for (int r = 0; r < mat3.size(); r++)
    {
        for (int c = 0; c < mat3[0].size(); c++)
        {
            cout << mat3[r][c] << endl;
        }
    }

    return 0;
}
