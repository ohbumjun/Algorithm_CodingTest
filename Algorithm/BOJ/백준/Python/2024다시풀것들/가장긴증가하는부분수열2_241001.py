# https://www.acmicpc.net/problem/12015

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000) ##

# 이진 탐색
def findPlace(tmp, val):
    lt = 1 # 어차피 tmp 맨 앞 0은 고려하지 않기 때문이
    rt = len(tmp) -1

    # 기존 이진 탐색과 다소 다르다
    # 일반적으로 이진 탐색은 tmp[mid] == val을 향해 찾아가지만
    # 여기는 tmp라는 배열 안에 정확한 val 값이 없을 수 있고
    # 현재 val이 들어갈 위치를 찾는 것이다. 그리고 그 위치는 lt, rt가 같은 
    while lt < rt :
        mid = ( lt + rt ) // 2
        if tmp[mid] < val : # val보다 작다면, 오른쪽 탐색
            lt = mid + 1
        elif tmp[mid] > val : # val보다 크다면, 왼쪽 탐색
            rt = mid 
        else : # lt와 rt가 가리키는 값이 똑같을 경우, 그곳이 새로운 val이 들어갈 위치
            lt = rt = mid
            break

    return lt
        

if __name__ == "__main__" :
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]
 
    # 탐색하면서, 현재 마지막 값보다 크면 맨 끝에 넣는다
    # 만약, 맨 끝값보다 작거나 같은 값이 나온다면
    # 이진탐색을 통해, 새로 만난 값이 위치를 찾은 다음
    # 해당 위치에 넣는다
    # 마지막에는 총 배열 길이 - 1 ( 0 을 처음에 임의로 추가했기 때문이다 ) 

    for i in range(len(arr)):
        if arr[i] > tmp[-1] : # tmp에 0을 미리 넣어주고 시작해야 tmp[-1]이 out of idx 에러 안뜬다 
            tmp.append(arr[i])
        else:
            newIdx = findPlace(tmp,arr[i])
            tmp[newIdx] = arr[i]

    print(len(tmp) - 1)
            
###
// https://www.codetree.ai/training-field/frequent-problems/problems/hide-and-seek?page=4&pageSize=5

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <cassert>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>
#include <sstream>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

// #define DEBUG 1

using namespace std;
int N;
vector<int> nums;
vector<int> LIS;

void Input()
{
	cin >> N;
	nums.resize(N);

	for (int n = 0; n < N; ++n)
		cin >> nums[n];
}


void Solve()
{
	LIS.push_back(nums[0]);
	for (int i = 1; i < N; ++i)
	{
		if (LIS.back() < nums[i])
		{
			LIS.push_back(nums[i]);
		}
		else
		{
			// LIS 에서 현재 원소가 들어갈 위치를 찾아서 넣어준다.
			// 단, 같은 원소는 ...?
			int insertIdx = -1;
			int left = 0;
			int right = LIS.size() - 1;

			while (left < right)
			{
				int midIdx = (left + right) / 2;

				// 더 작은 원소라면 오른쪽 탐색
				if (LIS[midIdx] < nums[i])
				{
					left = midIdx + 1;
				}
				else if (LIS[midIdx] > nums[i])
				{
					right = midIdx;
				}
				else if (LIS[midIdx] == nums[i])
				{
					left = midIdx;
					break;
				}
			}

			LIS[left] = nums[i];
		}
	}

	cout << LIS.size() << endl;
}

int main() {
	ios::sync_with_stdio(false);

	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input_c.txt", "r", stdin);

	Input();

	Solve();

	return 0;
}


###
