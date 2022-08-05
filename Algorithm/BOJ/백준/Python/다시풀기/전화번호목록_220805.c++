// https://www.acmicpc.net/problem/5052

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
#include <cstring>
#include <string>

#define endl "\n"
#define MAX 500 + 1
#define INF int(1e9)

using namespace std;

char vecString[10001][11];

struct Trie
{
    bool Finish;
    Trie* Node[10];
    Trie() :
        Finish(false)
    {
        for (int i = 0; i < 10; ++i)
            Node[i] = nullptr;
    }

    void insert(char* str)
    {
        if (*str == '\0')
        {
            Finish = true;
            return;
        }
        else
        {
            int curr = *str - '0';
            
            if (!Node[curr])
                Node[curr] = new Trie();

            Node[curr]->insert(str + 1);
        }
    }

    bool find(char* str)
    {
        // 마지막에 도달
        if (*str == '\0')
            return false;

        // 중간에 finish가 있다면 일관성 x (다른 단어가, 특정 단어의 접두어가 되는 상황)
        // 즉, 끝문자열이 아님에도, 해당 Trie 노드에서 Finish가 존재하는 상황
        if (Finish)
            return true;

        int curr = *str - '0';

        if (!Node[curr])
            return false;

        return Node[curr]->find(str + 1);
    }
};

int T, N;

void Input()
{
    cin >> T;
}

void Solve()
{
    for (int t = 0; t < T; ++t)
    {
        bool Consistency = true;
        Trie* Root = new Trie();

        cin >> N;

        for (int i = 0; i < N; ++i)
        {
            cin >> vecString[i];
            Root->insert(vecString[i]);
        }

        for (int i = 0; i < N; ++i)
        {
            if (Root->find(vecString[i]))
            {
                Consistency = false;
                break;
            }
        }

        if (Consistency)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
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
