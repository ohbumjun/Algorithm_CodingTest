https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=cpp

// 최초 풀이
#include <string>
#include <vector>
#include <iostream>
#include <stdlib.h>



using namespace std;

vector<int> totNums;
vector<int> winSizes;

int solution(vector<int> queue1, vector<int> queue2) {
    int answer = 0;
    int winSDiff = 1;
    long totN   = 0, targetN = 0;
    int stIdx  = -1, edIdx = -1;
    int initStIdx = 0, initEdIdx = queue1.size() - 1;
    
    for (int q : queue1) totNums.push_back(q);
    for (int q : queue2) totNums.push_back(q);
    for (int n : totNums) totN += n;
    targetN = totN / 2;
    
    winSizes.push_back(totNums.size() / 2);
    while(true)
    {
        winSizes.push_back(totNums.size() / 2 - winSDiff);
        winSizes.push_back(totNums.size() / 2 + winSDiff);
        winSDiff += 1;
        if (winSDiff >= totNums.size() / 2) break;
    }
    
    // for (int n : totNums) cout << n << ".";
    // cout << endl;
    
    // cout << "targetN : " << targetN << endl;
    // 1칸 짜리 sliding window ~ totNum.size() 만큼의 window 크기 모두 비교하기.
    for (int winIdx = 0; winIdx < winSizes.size(); ++winIdx)
    {
        long curN = 0; 
        int winSize = winSizes[winIdx];
        for (int idx = 0; idx < winSize; ++idx) curN += totNums[idx];
        if (curN == targetN)
        {
            stIdx = 0; edIdx = winSize - 1;
            break;
        }
        for (int idx = 1; idx <= totNums.size() - winSize; ++idx)
        {
            int prevIdx = idx - 1, nxtIdx = (idx + winSize - 1) % totNums.size();
            curN -= totNums[prevIdx];
            curN += totNums[nxtIdx];
            if (curN == targetN)
            {
                stIdx = idx; edIdx = idx + winSize - 1;
                break;
            }
        }
        
        if (stIdx != -1) break;
    }
    
    
    if (stIdx == -1 && edIdx == -1) return -1;
    
    // cout << "stIdx, edIdx : " << stIdx << "," << edIdx << endl;
    
    // cout << "stIdx - initStIdx : " << stIdx - initStIdx << endl;
    // cout << "edIdx - initEdIdx : " << edIdx - initEdIdx << endl;
    // if (stIdx >= totNums.size() / 2)
    {
        // answer += abs((int)totNums.size() - edIdx);
    }
    // else 
    {
        answer += abs(stIdx - initStIdx);
        answer += abs(edIdx - initEdIdx);
    }

    
    return answer;
}

// 정답 풀이 (투 포인터)
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    int answer = 0;
    vector<int> v;
    
    int s1 = 0;
    int e1 = queue1.size() - 1;
    int s2 = queue1.size();
    int e2 = queue1.size()*2 - 1;
    
    int size = queue1.size() * 2;
    long long sum1 = 0, sum2 = 0;
        
    for (int q1: queue1) {
        sum1 += q1;
        v.push_back(q1);
    }
    
    for (int q2: queue2) {
        sum2 += q2;
        v.push_back(q2);
    }

    // 위치가 원래대로 돌아오면 각 큐의 원소 합을 같게 만들 수 없음
    while (answer <= size * 2) {
        if (sum1 < sum2) {
            sum1 += v[(++e1) % size];
            sum2 -= v[(s2++) % size];
        } else if (sum1 > sum2) {
            sum1 -= v[(s1++) % size];
            sum2 += v[(++e2) % size];
        } else return answer; // 두 큐의 합이 같으면 answer 반환
        
        answer++;
    }
    
    return -1;
}


// 추가 정답 풀이 (찐 큐로 풀기)
#include <string>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    queue<int> q1 {{begin(queue1), end(queue1)}};
    queue<int> q2 {{begin(queue2), end(queue2)}};
    long long sum1 = accumulate(begin(queue1), end(queue1), 0ll);
    long long sum2 = accumulate(begin(queue2), end(queue2), 0ll);
    if((sum1 + sum2) % 2 != 0) return -1;
    size_t s1 = q1.size(), s2 = q2.size();
    int cnt = 0;
    while(sum1 != sum2) {
        if(cnt > s1 + s2 + 2) return -1;
        if(sum1 < sum2) {
            q1.push(q2.front());
            sum1 += q2.front();
            sum2 -= q2.front();
            q2.pop();
        }
        else {
            q2.push(q1.front());
            sum2 += q1.front();
            sum1 -= q1.front();
            q1.pop();
        }
        ++cnt;
    }
    return cnt;
}