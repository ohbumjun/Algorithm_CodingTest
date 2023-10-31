#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
 
#define endl "\n"
#define MAX 100000 + 1
using namespace std;
 
int N, M, Max_Cost, Start, End;
bool Visit[MAX];
vector<pair<int, int>> V[MAX];
 
int Bigger(int A, int B) { if (A > B) return A; return B; }
 
void Input()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int Pos1, Pos2, Cost;
        cin >> Pos1 >> Pos2 >> Cost;
        V[Pos1].push_back(make_pair(Pos2, Cost));
        V[Pos2].push_back(make_pair(Pos1, Cost));
        
        Max_Cost = Bigger(Max_Cost, Cost);
    }
 
    cin >> Start >> End;
}
 
bool BFS(int Cur_Cost)
{
    queue<int> Q;
    Q.push(Start);
    Visit[Start] = true;
 
    while (Q.empty() == 0)
    {
        int Cur_Factory = Q.front();
        Q.pop();
 
        if (Cur_Factory == End) return true;
 
        for (int i = 0; i < V[Cur_Factory].size(); i++)
        {
            int Next_Factory = V[Cur_Factory][i].first;
            int Next_Factory_Cost = V[Cur_Factory][i].second;
 
            if (Visit[Next_Factory] == false && Cur_Cost <= Next_Factory_Cost)
            {
                Visit[Next_Factory] = true;
                Q.push(Next_Factory);
            }
        }
    }
    return false;
}
 
void Solution()
{
    int Low = 0;
    int High = Max_Cost;
    while (Low <= High)
    {
        memset(Visit, false, sizeof(Visit));
        int Mid = (Low + High) / 2;
        if (BFS(Mid) == true) Low = Mid + 1;
        else High = Mid - 1;
    }
    cout << High << endl;
}
 
void Solve()
{
    Input();
    Solution();
}
 
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
   freopen("Input.txt", "r", stdin);
    Solve();
 
    return 0;
}


