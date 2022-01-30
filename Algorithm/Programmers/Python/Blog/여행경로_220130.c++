// https://programmers.co.kr/learn/courses/30/lessons/43164?language=cpp

#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <tuple>

using namespace std;

// Graph를 만들고
map<string, vector<pair<string, int>>> Graph;

// Check 배열 만들고
vector<bool> Check;

// 가능한 모든 경로를 담은 Vector
vector<vector<string>> AllPaths;
    
bool DFS(string stP, int N, int TotN, vector<string>& Path)
{
    if (N == TotN)
    {
        AllPaths.push_back(Path);
        return true;
    }
    
    size_t size = Graph[stP].size();
    for (size_t i = 0; i < size; i++)
    {
        // 다음 공항
        string NextPath = Graph[stP][i].first;
        // 해당 경로의 Index
        int Index       = Graph[stP][i].second;
        // 이미 사용한 경로라면 Pass
        if (Check[Index])
            continue;
        // 사용 경로 표시 
        Check[Index] = true;
        // 경로 추가
        Path.push_back(NextPath);
        // DFS
        DFS(Graph[stP][i].first, N + 1, TotN, Path);
        // 사용 경로 해제 
        Check[Index] = false;
        // 경로 해제 
        Path.pop_back();
    }
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    
    Check = vector<bool>(tickets.size());

    // 그래프 형태 == (시작 위치) : (도착 위치, 경로 Index)
    size_t Size = tickets.size();
    for (size_t i = 0; i < Size; i++)
    {
        Graph[tickets[i][0]].push_back(make_pair(tickets[i][1], i));
    }
    
    // "ICN" 에서 시작
    vector<string> Path = {"ICN"};
    DFS("ICN", 1, tickets.size() + 1, Path);
    
    // 마지막 경로 알파벳 정렬
    sort(AllPaths.begin(), AllPaths.end());
    
    return AllPaths[0];
}