https://school.programmers.co.kr/learn/courses/30/lessons/135807

#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

// 최대 공약수를 구해주는 함수
int lcm(int a, int b)
{
    int t;
    
    while(b != 0)
    {
        t = a % b;
        a = b;
        b = t;
    }
    
    return a;
}

int checkNotDivided(vector<int>& array, int div)
{
    for (int num : array) 
        if (num % div == 0) 
            return 0;
    return div;
}

int solution(vector<int> arrayA, vector<int> arrayB) {
    
    // 방향
    // 1) 각 array 의 최대공약수를 구한다 (조건을 만족하는 최대 크기의 숫자를 구하는 것)
    // 2) arrayA 의 최대공약수로 arrayB 를 나눠보고, 그 반대도 수행
    // 조건 만족하는 최대 숫자를 리턴
    int answer = 0;
    
    int lcm_a = arrayA[0];
    int lcm_b = arrayB[0];
    
    // 기존 최대공약수와, 현재 array 원소 간의 최대 공약수를 구해가는 것일까 ?
    // - 기존 최대공약수가 나눠질 수 있다면, 지금까지 조사한 원소들도 나눠질 수 있는 숫자라는 것.
    // - 어떻게 보면, 점차 범위를 좁혀가되, 지속해서 큰 값을 유지하고 싶은 것이다.
    for (int n : arrayA) lcm_a = lcm(lcm_a, n);
    for (int n : arrayB) lcm_b = lcm(lcm_b, n);
    
    answer = checkNotDivided(arrayA, lcm_b);

    // 맨 처음 풀이에서는, lcm_a, lcm_b 가 둘다 조건에 만족할 수 있다는
    // 것을 간과했다.
    answer = max(checkNotDivided(arrayB, lcm_a), answer);
    
    return answer; 
}

