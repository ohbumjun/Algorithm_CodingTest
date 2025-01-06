// https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=cpp

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int maxTime = 1000000000;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end());
    // 핵심 
    // 1) 해당 시간 안에 처리할 수 있는 사람 수 -> 
    //  "특정 시간" 을 각 심사 시간 으로 나눈 합
    // 2) long long 으로의 변환
    // 3) 이분 탐색 -> 최소 0, minT < maxT / 최소 1 , minT <= maxT
    long long minT = 1, maxT = (long long)times[times.size() - 1] * n;
    
    while(minT < maxT)
    {
        long long midT = (minT + maxT) / 2;
        long long totN = 0;
        
        for (long long time : times)
        {
            totN += midT / time;    
        }
        
        if (totN >= n)
        {
            maxT = midT - 1;
            answer = midT;
        }
        else 
        {
            minT = midT + 1;
        }
    }
    
    return answer;
}