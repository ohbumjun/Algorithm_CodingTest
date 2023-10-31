#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

vector<string> solution(vector<string> record) {
    
    // Enter, Leave 의 경우, 별도의 vector 에  모아둘 것이다.
    int recSize = record.size();
    
    vector<string> answer;
    vector<vector<string>> vecInOut;
    unordered_map<string, string> mapId;
    
    vecInOut.reserve(recSize);
    
    for (int i = 0; i < recSize; ++i)
    {
        vector<string> vecCmd;
        vecCmd.reserve(3);
        
        int cur = 0, prev = 0;
        
        cur = record[i].find(' ');
        
        while (cur != string::npos)
        {
            const string& subStr = record[i].substr(prev, cur - prev);
            vecCmd.push_back(subStr);
            prev = cur + 1;
            cur = record[i].find(' ', prev);
            
            if (cur == string::npos)
            {
                const string& subStr = record[i].substr(prev, cur - prev);
                vecCmd.push_back(subStr);
            }
        }
        
        if (vecCmd[0] == "Leave")
            vecInOut.push_back(vecCmd);
        if (vecCmd[0] == "Enter")
        {
            // vecInOut Map 에 Insert 하기
            vecInOut.push_back(vecCmd);
            
            // ID Change
            mapId[vecCmd[1]] = vecCmd[2];
        }
        if (vecCmd[0] == "Change") 
        {
            // ID Change
            mapId[vecCmd[1]] = vecCmd[2];
        }
    }
    
    for (int i = 0; i < vecInOut.size(); ++i)
    {
        if (vecInOut[i][0] == "Enter")
            answer.push_back(mapId[vecInOut[i][1]]+"님이 들어왔습니다.");
        else 
            answer.push_back(mapId[vecInOut[i][1]]+"님이 나갔습니다.");
    }
    
    
    return answer;
}