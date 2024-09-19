// https://school.programmers.co.kr/learn/courses/30/lessons/131130?language=cpp

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int getNotVisited(const vector<bool>& visited)
{
    int idx = -1;
    
    for (int i = 0; i < visited.size(); ++i)
    {
        if (visited[i] == false)
        {
            idx = i;
            break;
        }
    }
    
    return idx;
}

void getMaxVal(int curIdx, vector<int>& idxs, int &maxVal, int groupCnt, 
              const vector<vector<int>>& combinations)
{
    if (idxs.size() == 2)
    {
        int fIdx = idxs[0];
        int sIdx = idxs[1];
        
        int curVal = combinations[fIdx].size() * combinations[sIdx].size();
        
        maxVal = max(curVal, maxVal);
        return;
    }
    
    for (int grpIdx = 0; grpIdx < groupCnt; ++grpIdx)
    {
        if (grpIdx == curIdx) 
            continue;
        idxs.push_back(grpIdx);
        getMaxVal(grpIdx, idxs, maxVal, groupCnt, combinations);
        idxs.pop_back();
    }
}

int solution(vector<int> cards) 
{
    int groupCnt = 0;
    vector<bool> visited(cards.size(), false);
    vector<vector<int>> combinations;
    combinations.resize(cards.size());

    int firstSum = 0;
    int secondSum = 0;

    vector<int> firstGroup;
    firstGroup.reserve(cards.size());

    vector<int> secondGroup;
    secondGroup.reserve(cards.size());

    while (true)
    { 
        int nxtIdx = getNotVisited(visited);
        if (nxtIdx == -1)
            break;
        while (visited[nxtIdx] == false)
        {
            int curNum = cards[nxtIdx] - 1;
            combinations[groupCnt].push_back(curNum);
            visited[nxtIdx] = true;
            int nxtNum = cards[nxtIdx] - 1;
            nxtIdx = nxtNum;
        }
        groupCnt += 1;
    }
    
    if (groupCnt == 1)
        return 0;
    
    int maxVal = 0;
    vector<int> idxs;
    getMaxVal(-1, idxs, maxVal, groupCnt, combinations);
    
    return maxVal;
}