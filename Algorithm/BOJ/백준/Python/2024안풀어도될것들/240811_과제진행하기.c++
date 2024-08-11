// https://school.programmers.co.kr/learn/courses/30/lessons/176962#

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>
#include <queue>
#include <sstream>


using namespace std;

vector<string> splitString(const string& str, char delimiter) 
{
    vector<string> ret;
    string token;
    stringstream ss(str);
    while (getline(ss, token, delimiter)) 
  	{
        ret.push_back(token);
    }
    return ret;
}
struct Assign
{
    string name;    // 중복 X
    int stTime;     // 시작 시간
    int playTime;
    
    bool operator < (const Assign& other)
    {
        return stTime < other.stTime;
    }
};

// 잠시 멈춘 과제를 저장해둔 Stack 
stack<Assign> stopped;
queue<Assign> todos;

vector<string> solution(vector<vector<string>> plans) {
    int curTime = 0;
    vector<string> answer;
    vector<Assign> assigns;
    
    for (const vector<string>& plan : plans)
    {
        Assign assign;
        assign.name     = plan[0];
        assign.playTime = stoi(plan[2]);
        vector<string> times = splitString(plan[1], ':');
        assign.stTime   = stoi(times[0]) * 60 + stoi(times[1]);
        
        assigns.push_back(assign);
    }
    
    sort(assigns.begin(), assigns.end());
    
    for (Assign& assign : assigns) todos.push(assign);
    
    while(todos.empty() == false)
    {
        Assign& curAssign = todos.front();
        todos.pop();
        curTime = curAssign.stTime;
        
        if (todos.empty())
        {
            answer.push_back(curAssign.name);
            
            while(stopped.empty() == false)
            {
                Assign& stop = stopped.top();
                stopped.pop();
                answer.push_back(stop.name);
            }
        }
        else 
        {
            Assign& nxtAssign = todos.front();
            
            if (curAssign.stTime + curAssign.playTime > nxtAssign.stTime)
            {
                curTime = nxtAssign.stTime;
                curAssign.playTime = curAssign.stTime + curAssign.playTime - nxtAssign.stTime;
                stopped.push(curAssign);
            }
            else 
            {
                answer.push_back(curAssign.name);
                curTime = curAssign.stTime + curAssign.playTime;
                while(stopped.empty() == false)
                {
                    Assign& stop = stopped.top();
                    // cout << "stop name : " << stop.name << endl;
                    int stopEndTime = curTime + stop.playTime;
                    if (stopEndTime <= nxtAssign.stTime)
                    {
                        answer.push_back(stop.name);
                        curTime = stopEndTime;
                        stopped.pop();
                    }
                    else 
                    {
                        stop.playTime = stopEndTime - nxtAssign.stTime;
                        curTime = nxtAssign.stTime;
                        break;
                    }
                }
            }
        }
    }
    
    return answer;
}