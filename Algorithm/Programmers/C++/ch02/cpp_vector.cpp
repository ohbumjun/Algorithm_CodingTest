
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
    vector<int> v1;
    vector<int> v2(10); // 10개의 정수 할당하여 사용 --> v2[0] ~ v2[9] 까지 사용 가능, 0으로 초기화
    vector<int> v3(10,1); // 10개 정수, 1로 초기화 

    // v1
    v1.push_back(10);
    v1.push_back(20);

    return 0;
}

