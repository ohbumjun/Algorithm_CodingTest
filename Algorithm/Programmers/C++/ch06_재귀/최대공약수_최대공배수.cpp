#include <iostream>
#include <numeric>

// 최대 공약수
// 유클리드 알고리즘 ( 유클리드 호제법 )
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
};

// 최소 공배수
// 두 정수의 곱은, 두 정수의 최대 공약수와, 최소 공배수의 곱과 같다는 성질을 이용해서 구할 수 있다
// a * b ==  gcd(a,b) * lcm(a,b);
int lcm(int a, int b)
{
    return (a * b) / gcd(a, b);
}

// 최대 공약수, 최소 공배수 계산함수
/*
template<class M, class N>
constexpr std::common_type<M,N> gcd(M m, N n);

template<class M, class N>
constexpr std::common_type<M,N> lcm(M m, N n);
*/

int main()
{
    int gcd1 = gcd(10, 15);
    int lcm1 = lcm(10, 15);

    int gcd2 = std::gcd(10, 15);
    int lcm2 = std::lcm(10, 15);
    return 0;
}