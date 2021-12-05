#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include<vector>
#include <algorithm>
#include <functional>
#include<queue>
 
#define endl "\n"
#define NODE_MAX 500 + 1
#define EDGE_MAX 6000 + 1
#define INF int(1e9)

using namespace std;

int N, M, start;
vector<pair<pair<int, int>, int>> edges;
long long dist[NODE_MAX];


void input()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int stN, edN, cost;
        cin >> stN >> edN >> cost;
        edges.push_back(make_pair(make_pair(stN, edN), cost));
    }

    // 최단 거리 정보 초기화
    fill_n(dist, NODE_MAX, INF);
}

void solve(int stN)
{
    dist[stN] = 0;
    for (int i = 0; i < N - 1; i++)
    {
        for (int j = 0; j < M; j++)
        {
            int stN  = edges[j].first.first;
            int edN = edges[j].first.second;
            int cost = edges[j].second;
            if (dist[stN] != INF && dist[edN] > dist[stN] + cost)
            {
                dist[edN] = dist[stN] + cost;
            }
        }
    }
    for (int j = 0; j < M; j++)
    {
        int stN = edges[j].first.first;
        int edN = edges[j].first.second;
        int cost = edges[j].second;
        if (dist[stN] != INF && dist[edN] > dist[stN] + cost)
        {
            cout << -1 << endl;
            return;
        }
    }
    for (int i = 2; i <= N; i++)
    {
        if (dist[i] == INF)
            cout << -1 << "\n";
        else
            cout << dist[i] << "\n";
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
     freopen("input_C.txt", "r", stdin);
   input();
   solve(1);
 
    return 0;
}

/*
dist의 type을
int 에서 long long 형태로 바꿔줘야 하는 이유?


이 문제에서 출력 초과가 발생하는 이유는 -1을 출력해야 하는 상황에서 각 도시로 가는 최단 거리들을 출력하기 때문입니다.

질문하신 내용처럼 기존 dist에 들어있는 INF가 초과되어 overflow가 발생하지는 않으나, 이 문제는 가중치가 음수인 것이 허용되는 벨만-포드 알고리즘 문제입니다. 음수 사이클이 존재한다면 끝 없이 최소값이 갱신될 수 있고 이 때문에 출력초과가 발생하는 것입니다.

왜 이 때문에 출력초과가 발생하느냐? 가 궁금하실텐데 결론부터 말하자면 underflow때문입니다. 문제에서 주어진 조건인 정점의 개수가 500개, 간선의 개수가 6000개, 최소 가중치가 -10000이라면 충분히 underflow가 발생할 수 있는 수치입니다. (-500 * 6000 * 10000 = -3 * 10^10, Integer.MIN_VALUE = 약 -2*10^9)

우선 -1을 출력하는 조건은 '정점의 개수를 V라 할 때, V - 1번 만큼 최소값을 충분히 갱신해주고 V번째에서 최소값이 갱신 되는 경우' 입니다.

그리고 이런 경우가 있다고 가정해봅시다.

- 정점 V: 500개 (1에서 출발)

- 간선 E: 6000개 (1에서 2로 가며 가중치는 -10000, 2에서 1로가며 가중치는 -10000 ...반복 ...)

벨만-포드 알고리즘에서의 내부 반복문이 1번 회전한다면 2로 가는 비용은 -10000로 갱신, 3번 회전한다면 2로 가는 비용은 -30000으로 갱신됩니다. 이런 과정을 거쳐서 외부 반복문이 한 번 회전한다면 2로 가는 비용은 -60000000로 갱신됩니다. 한번의 회전으로 이미 충분히 낮은 숫자가 됐다고 직감하실 수 있을 겁니다. 위의 경우을 실제로 돌려보니 V = 466만 해도 이미 언더플로우가 나버려서 최소값 갱신이 불가능합니다. 즉, dist를 long으로 설정해줘야 정상적인 음의 값으로 갱신할 수 있기 때문에 벨만-포드 알고리즘에서 음수 사이클이 존재한다고 판정할 수 있는 것입니다.
*/
