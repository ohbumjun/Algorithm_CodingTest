# https://www.acmicpc.net/problem/17298

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
sys.setrecursionlimit(10000)

'''
이 문제는 스택을 사용한다.
특이한 점은, 스택에 일반적인 경우와 같이
값을 저장하는 것이 아니라,
idx를 저장한다는 것이다.

최종적인 답. 인 result 배열을 선언해준다.
오큰수가 없는 idx 값을 위해 모든 원소를 -1로 초기화해준다

stack에는 idx가 들어간다고 했다.
우리는 stack의 맨 위 값, 즉 stack 맨위에 저장된 idx,
그 idx에 위치한 값과,

현재 우리가 보고 있는 nums[i]라는 값을 비교한다.
우리는 맨 앞에서부터 갈 것이다.

무슨 말이냐면, 현재 nums[i]와 , stack 에 있는 값들을
볼 수 있을 때까지 계속 볼것이다.

여튼, nums[i]가 더 크면
result[stack[-1]] = nums[i]를 저장해준다.
그리고, 다시 stack에서 pop을 시키고

현재 nums[i]와 stack의 맨 위의 값을 비교한다. //
이 과정을 반복한다.

언제까지 ? stack이 빌때까지

만약 stack이 비거나, stack[-1]  > nums[i]라면
그냥 현재 i를 stack에 넣고
i는 1 증가시켜준다.

'''

n = int(input())
nums = list(map(int,input().split()))
result = [ -1 for _ in range(n) ]
stack = [0]
i = 1

for i in range(1,len(nums)) :
    while stack and nums[ stack[-1] ] < nums[i] :
        result[ stack[-1] ] = nums[i]
        stack.pop()

    stack.append(i)


print(*result)
    



'''
#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <array>
#include <list>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

// 3, 5, 2, 7
// - 2, 3, 5, 7
// - (7:-1), (5:7), (3:5), (2:7)
// - 3,5,7

// 7, 1, 3, 6, 9
// - 1, 3, 6, 7, 9
// - (7:9), (3:9)

// 8. 6. 2. 1. 7, 4
// - 1, 2, 4, 6, 7, 8,
// - (8:-1), (6:7), (2:7), (1:7), (7:-1), (4:-1)


int N;
vector<int> vecInt;
vector<int> resultInt;
stack<int> stkInt;

void Input()
{
    cin >> N;
    vecInt.reserve(N);
    resultInt = vector<int>(N, -1);

    int Input;

    // 나보다 크면서, 가장 왼쪽
    // 이분탐색을 하려면, 정렬된 형태이어야 한다.
    // 해당 원소가 나의 idx 보다 작다면, 
    for (int idx = 0; idx < N; ++idx)
    {
        int Input;
        cin >> Input;
        vecInt.push_back(Input);
    }
}


void Solve()
{
   for (int idx = 0; idx < N; ++idx)
   {
	   while (!stkInt.empty() && vecInt[stkInt.top()] < vecInt[idx])
	   {
           int topIdx = stkInt.top();

           if (vecInt[topIdx] < vecInt[idx])
           {
               resultInt[topIdx] = vecInt[idx];
               stkInt.pop();
           }
	   }
       stkInt.push(idx);
   }

    for (int i = 0; i < N; ++i)
    {
        cout << resultInt[i] << " ";
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin); //

    Input();

    Solve();
    
    return 0;
}
'''