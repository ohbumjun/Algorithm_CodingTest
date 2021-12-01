#include <iostream>
#include <algorithm>

bool binary_search(int data[], int n, int target)
{
    int lower = 0;
    int upper = n - 1;

    // 범위를 벗어남 
    if(data[lower] > target || data[upper] < target)
        return false;

    while (lower <= upper)
    {
        int mid = (lower + upper) / 2;
        if (data[mid] == target)
            return true;
        else if (data[mid] < target)
            lower = mid + 1;
        else
            upper = mid - 1;
    }
    return false;
}

/*
C++ binary_searh 

template <class ForwardIt, class T>
bool binary(ForwardIt first, ForwardIt last, const T& value);

template <class ForwardIt, class T, class Compare>
bool binary(ForwardIt first, ForwardIt last, const T& value, Compare comp);

정렬된 컨테이너 first ~ last 범위 안에서, value 값이 있는지를 검사한다.
최소 first ~ last 범위 안에서라도, 정렬이 되어 있어야 동작한다.

기본적으로 < 연산자를 이용해서 값을 비교하고, 비교 함수 comp를 지정할 수도 있다.


*/

using namespace std;

int main()
{
    int data[] = {1, 2, 3, 4, 7, 10, 15, 18, 23, 25, 27, 29, 31};
    int target = 23;

    // bool res1 = linear_search(data, std::size(data), target);
    bool res1 = binary_search(data, std::size(data), target);
    bool res2 = std::binary_search(std::begin(data), std::end(data), target);

    cout << res1 << endl;
    cout << res2 << endl;

    return 0;
}