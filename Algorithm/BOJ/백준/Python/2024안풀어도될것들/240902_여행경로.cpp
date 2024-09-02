#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <tuple>

using namespace std;

unordered_map<string, vector<string>> graphs;
unordered_map<string, vector<bool>> visited;
vector<string> answer;
int totPathCnt;

void dfs(const string& st, int accCnt, vector<string>& path)
{
    if (answer.size() > 0) return;
    
    if (totPathCnt == accCnt)
    {
        answer = path;
        return;
    }
    
    for (int idx = 0; idx < graphs[st].size(); ++idx)
    {
        if (visited[st][idx]) continue;
        const string& nxt = graphs[st][idx];
        
        visited[st][idx] = true;
        path.push_back(nxt);
        
        dfs(nxt, accCnt + 1, path);
        
        visited[st][idx] = false;
        path.pop_back();
    }
}

vector<string> solution(vector<vector<string>> tickets) 
{
    totPathCnt = tickets.size();
    
    for (const vector<string>& path : tickets)
    {
        const string& st = path[0];
        const string& ed = path[1];
        graphs[st].push_back(ed);
        visited[st].push_back(false);
    }
    
    for (auto it = graphs.begin(); it != graphs.end(); ++it) 
    {
        vector<string>& path = it->second;
        sort(path.begin(), path.end());
    }
    
    vector<string> path;
    path.push_back("ICN");
    dfs("ICN", 0, path);
    
    return answer;
}