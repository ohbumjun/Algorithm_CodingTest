// https://www.codetree.ai/training-field/frequent-problems/problems/codetree-tour/description?page=1&pageSize=10

// 1) 시간 초과
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <algorithm>
#include <cassert>
using namespace std;

#define INT_MAX int(1e9)

int Q, N, M;

int minDist[2000][2000];

struct Product
{
    int id;
    int start = 0;
    int revenue;
    int dest;

    bool operator < (const Product& other) const
    {
        int curCost = minDist[start][dest];
        int otherCost = minDist[other.start][other.dest];
        if (revenue - curCost != other.revenue - otherCost)
            return revenue - curCost < other.revenue - otherCost; // 순수익 더 큰게 위로
        return id > other.id; // id 작은게 위로
    }
};

int currentStart = 0;

unordered_map<int, Product> products;
priority_queue<Product> productQueue;
unordered_map<int, vector<pair<int, int>>> graph; // city, weight

void Input()
{
    cin >> Q; // 100,000
}

int findBest() // logN 으로 줄여야 한다.
{
    int bestId = -1;

    // 매번 최적 여행 상품 판매할 때마다, cost update 하면 안된다....
    // 그냥 여기서는 priority_queue 에서 pop 만 하면 되지 않을까 ?
    // 그리고 비용 계산은, 맨 처음이랑 출발지 변경할 때만
    // 그러면, 여행 상품 새로 생성할 때는 ? 이것도...30,000번이다.
    // 즉, 1) 여행 상품 판매할 때마다 2) 여행 상품 새로 생성할 때마다
    // 매번 cost update 를 해서는 안된다는 것이다.
    // 왜 안되는 거지 ? 어차피 n 번 (2000) 수행하는 거자나.

    // 1) 출발지 변경시 : 15 * 2000 * 2000 = 60,000,000
    // 2) 새로운 여행 상품 추가 : 30000 * 2000 = 60,000,000
    while (!productQueue.empty())
    {
        auto product = productQueue.top();

        // 도달불가의 경우, 판매 불가
        int cost = minDist[product.start][product.dest];
        if (product.revenue - cost < 0)
        {
            break;
        }
        productQueue.pop();

        // 여기서 pop 한 product 의 id 가 이미 사라진 녀석일 수 있다
        if (products.find(product.id) == products.end())
            continue;

        bestId = product.id;
        products.erase(product.id);
        break;
    }

    return bestId;
}

void getCost(int cur, int dest, int accDist, vector<bool>& visit, int& cost)
{
    if (cur == dest)
    {
        cost = min(cost, accDist);
        return;
    }
    visit[cur] = true;
    for (const auto& nextInfo : graph[cur])
    {
        int nxtCity = nextInfo.first;
        int nxtWeight = nextInfo.second;
        if (visit[nxtCity])
            continue;
        getCost(nxtCity, dest, accDist + nxtWeight, visit, cost);
    }
    visit[cur] = false;
}

void updateCosts()
{
    // 1) 시간 초과 : 2000 * 2000 * 2000 = 8,000,000,000 이여서 10^9...이정도면 시간초과
    // for (int k = 0; k < N; ++k) // k 가 가장 먼저 ! . 해당 k 노드를 거쳐가는 것을 차례대로 update
    // {
    //     for (int f = 0; f < N; ++f)
    //     {
    //         for (int s = 0; s < N; ++s)
    //         {
    //             if (k == f || k == s)
    //                 continue;
    //             if (minDist[f][k] == INT_MAX || minDist[k][s] == INT_MAX)
    // 				continue;
    //             minDist[f][s] = min(minDist[f][s], minDist[f][k] + minDist[k][s]);
    //         }
    //     }
    // }

    // 2) 이미 구한 것을 또 다시 구해야 하는 경우가 있다.
    // for (auto& product : products)
    // {
    //     int start = product.second.start;
    //     int dest = product.second.dest;
    //     int cost = INT_MAX;
    //     vector<bool> visit(N, false);
    //     getCost(start, dest, 0, visit, cost);
    //     product.second.cost = cost;
    // }

    // 3) 다익스트라 알고리즘 -> 시간 초과
    for (int stN = 0; stN < N; ++stN)
    {
        if (graph.find(stN) == graph.end())
			continue;
        vector<int> minDistTemp(N, INT_MAX);
        for (int s = 0; s < N; ++s)
            minDistTemp[s] = minDist[stN][s];
        priority_queue<pair<int, int>> pqueue;
        pqueue.push({ 0, stN });
        minDistTemp[stN] = 0;

        while (!pqueue.empty())
        {
            pair<int,int> top = pqueue.top();
            pqueue.pop();
            int curDist = -top.first;
            int curCity = top.second;
            for (const pair<int, int>& nextInfo : graph[curCity])
            {
				int nextCity = nextInfo.first;
				int nextDist = nextInfo.second + curDist;
                if (minDistTemp[nextCity] <= nextDist)
                    continue;
				minDistTemp[nextCity] = nextDist;
				pqueue.push({ -minDistTemp[nextCity], nextCity });
			}
        }

        for (int c = 0; c < N; ++c)
        {
			minDist[stN][c] = min(minDist[stN][c], minDistTemp[c]);
            minDist[c][stN] = min(minDist[c][stN], minDist[stN][c]);
		}
    }
}

void Solve()
{
    /*
    >> n 개 도시, m 개 간선
    각 도시 0번 ~ n - 1 번 번호
    방향성 x
    2개 도시 사이 간선 여러개 가능
    자기 자신으로의 간선 가능
    출발지는 항상 0번 도시

    >> 5가지 명령어
    3) 여행 상품 취소
    - 고유 식별자 id 여행 상품 존재 --> 해당 id 여행 상품을
     관리 목록에서 삭제
    4) 최적 상품 판매
    - 조건 : revenue - cost 가 최대
    - 같은 값 : id 가 가장 작은 것
    - cost 는 출발지 부터 dest 까지 도달하기 위한 최단 거리
    - dest 도달 불가 or cost > revenue 이면 판매 불가
      즉, 판매 "가능" 상품 중, 우선 순위 높은 1개 판매
      해당 id 출력
      관리 목록에서 제외
      if 판매 가능 상품 없으면 -1 출력하고 상품 제거

    5) 여행 상품 출발지 변경
    - 전부 출발지를 s 로 변경하는 명령어
    - 출발지 변경에 따라 각 상품의 cost 가 변경될 수 있음
    */

    for (int q = 0; q < Q; ++q)
    {
        int cmd;
        cin >> cmd;

        switch (cmd)
        {
        case 100:
        {
            cin >> N;
            cin >> M;
            for (int r = 0; r < N; ++r)
            {
                for (int c = 0; c < N; ++c)
                {
                    if (r == c)
                        minDist[r][c] = 0;
                    else
                        minDist[r][c] = INT_MAX;
                }
            }
            for (int m = 0; m < M; ++m)
            {
                int city1, city2, weight;
                cin >> city1 >> city2 >> weight;
                if (city1 == city2)
                {
                    weight = 0;
                }
                graph[city1].push_back({ city2, weight });
                graph[city2].push_back({ city1, weight });
                // minDist[city1][city2] = min(minDist[city1][city2], weight);
                // minDist[city2][city1] = min(minDist[city2][city1], weight);
            }
            updateCosts();

            // 출력
            // cout << "----------------------" << endl;
            // for (const auto& info : graph)
            // {
            //     cout << info.first << " : ";
            //     for (const auto& nextInfo : info.second)
            //         cout << nextInfo.first << " " << nextInfo.second << " / ";
            // 	cout << endl;
            // }

            break;
        }
        case 200:
        {
            int id, revenue, dest;
            cin >> id >> revenue >> dest;
            products[id] = { id, currentStart, revenue, dest };
            // updateSingleCost(id);
            productQueue.push(products[id]);
            break;
        }
        case 300:
        {
            int id;
            cin >> id;
            if (products.find(id) != products.end())
            {
                products.erase(id);
            }
            break;
        }
        case 400:
        {
            int bestId = findBest();
            cout << bestId << endl;
            break;
        }
        case 500:
        {
            int s;
            cin >> s;
            currentStart = s;
            for (auto& product : products)
            {
                product.second.start = s;
            }

            // queue 를 모두 비워주고, 다시 products 내용을 queue 에 넣어준다.
            while (!productQueue.empty())
            {
                productQueue.pop();
            }
            for (auto& product : products)
            {
                productQueue.push(product.second);
            }

            break;
        }
        }
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

// 2) 다익스트라 : 모든 정점 x -> start 에 대해서만 진행
// https://www.codetree.ai/training-field/frequent-problems/problems/codetree-tour/description?page=1&pageSize=10

// 1) 시간 초과
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <algorithm>
#include <cassert>
using namespace std;

#define INT_MAX int(1e9)

int Q, N, M;

int minDist[2001];

struct Product
{
    int id;
    int start = 0;
    int revenue;
    int dest;

    bool operator < (const Product& other) const
    {
        int curCost = minDist[dest];
        int otherCost = minDist[other.dest];
        if (revenue - curCost != other.revenue - otherCost)
            return revenue - curCost < other.revenue - otherCost; // 순수익 더 큰게 위로
        return id > other.id; // id 작은게 위로
    }
};

int currentStart = 0;

unordered_map<int, Product> products;
priority_queue<Product> productQueue;
unordered_map<int, vector<pair<int, int>>> graph; // city, weight

void Input()
{
    cin >> Q; // 100,000
}

int findBest() // logN 으로 줄여야 한다.
{
    int bestId = -1;

    // 매번 최적 여행 상품 판매할 때마다, cost update 하면 안된다....
    // 그냥 여기서는 priority_queue 에서 pop 만 하면 되지 않을까 ?
    // 그리고 비용 계산은, 맨 처음이랑 출발지 변경할 때만
    // 그러면, 여행 상품 새로 생성할 때는 ? 이것도...30,000번이다.
    // 즉, 1) 여행 상품 판매할 때마다 2) 여행 상품 새로 생성할 때마다
    // 매번 cost update 를 해서는 안된다는 것이다.
    // 왜 안되는 거지 ? 어차피 n 번 (2000) 수행하는 거자나.

    // 1) 출발지 변경시 : 15 * 2000 * 2000 = 60,000,000
    // 2) 새로운 여행 상품 추가 : 30000 * 2000 = 60,000,000
    while (!productQueue.empty())
    {
        auto product = productQueue.top();

        // 도달불가의 경우, 판매 불가
        int cost = minDist[product.dest];
        if (product.revenue - cost < 0)
        {
            break;
        }
        productQueue.pop();

        // 여기서 pop 한 product 의 id 가 이미 사라진 녀석일 수 있다
        if (products.find(product.id) == products.end())
            continue;

        bestId = product.id;
        products.erase(product.id);
        break;
    }

    return bestId;
}

void getCost(int cur, int dest, int accDist, vector<bool>& visit, int& cost)
{
    if (cur == dest)
    {
        cost = min(cost, accDist);
        return;
    }
    visit[cur] = true;
    for (const auto& nextInfo : graph[cur])
    {
        int nxtCity = nextInfo.first;
        int nxtWeight = nextInfo.second;
        if (visit[nxtCity])
            continue;
        getCost(nxtCity, dest, accDist + nxtWeight, visit, cost);
    }
    visit[cur] = false;
}

void updateCosts()
{
    // 1) 시간 초과 : 2000 * 2000 * 2000 = 8,000,000,000 이여서 10^9...이정도면 시간초과
    // for (int k = 0; k < N; ++k) // k 가 가장 먼저 ! . 해당 k 노드를 거쳐가는 것을 차례대로 update
    // {
    //     for (int f = 0; f < N; ++f)
    //     {
    //         for (int s = 0; s < N; ++s)
    //         {
    //             if (k == f || k == s)
    //                 continue;
    //             if (minDist[f][k] == INT_MAX || minDist[k][s] == INT_MAX)
    // 				continue;
    //             minDist[f][s] = min(minDist[f][s], minDist[f][k] + minDist[k][s]);
    //         }
    //     }
    // }

    // 2) 이미 구한 것을 또 다시 구해야 하는 경우가 있다.
    // for (auto& product : products)
    // {
    //     int start = product.second.start;
    //     int dest = product.second.dest;
    //     int cost = INT_MAX;
    //     vector<bool> visit(N, false);
    //     getCost(start, dest, 0, visit, cost);
    //     product.second.cost = cost;
    // }

    // 3) 다익스트라 알고리즘 -> 시간 초과
   // for (int stN = 0; stN < N; ++stN)
   // {
   //     if (graph.find(stN) == graph.end())
   //         continue;
   //     vector<int> minDistTemp(N, INT_MAX);
   //     priority_queue<pair<int, int>> pqueue;
   //     pqueue.push({ 0, stN });
   //     minDistTemp[stN] = 0;
   // 
   //     while (!pqueue.empty())
   //     {
   //         pair<int, int> top = pqueue.top();
   //         pqueue.pop();
   //         int curDist = -top.first;
   //         int curCity = top.second;
   //         for (const pair<int, int>& nextInfo : graph[curCity])
   //         {
   //             int nextCity = nextInfo.first;
   //             int nextDist = nextInfo.second + curDist;
   //             if (minDistTemp[nextCity] <= nextDist)
   //                 continue;
   //             minDistTemp[nextCity] = nextDist;
   //             pqueue.push({ -minDistTemp[nextCity], nextCity });
   //         }
   //     }
   // 
   //     for (int c = 0; c < N; ++c)
   //     {
   //         minDist[stN][c] = min(minDist[stN][c], minDistTemp[c]);
   //     }
   // }

    // 4) 다익스트라 -> 현재 시작 start 로부터만 구하기
    for (int c = 0; c < N; ++c)
        minDist[c] = INT_MAX;
    minDist[currentStart] = 0;

    priority_queue<pair<int, int>> pqueue;
    pqueue.push({ 0, currentStart });

    while (!pqueue.empty())
    {
        pair<int, int> top = pqueue.top();
        pqueue.pop();
        int curDist = -top.first;
        int curCity = top.second;
        for (const pair<int, int>& nextInfo : graph[curCity])
        {
            int nextCity = nextInfo.first;
            int nextDist = nextInfo.second + curDist;
            if (minDist[nextCity] <= nextDist)
                continue;
            minDist[nextCity] = nextDist;
            pqueue.push({ -minDist[nextCity], nextCity });
        }
    }
}

void Solve()
{
    /*
    >> n 개 도시, m 개 간선
    각 도시 0번 ~ n - 1 번 번호
    방향성 x
    2개 도시 사이 간선 여러개 가능
    자기 자신으로의 간선 가능
    출발지는 항상 0번 도시

    >> 5가지 명령어
    3) 여행 상품 취소
    - 고유 식별자 id 여행 상품 존재 --> 해당 id 여행 상품을
     관리 목록에서 삭제
    4) 최적 상품 판매
    - 조건 : revenue - cost 가 최대
    - 같은 값 : id 가 가장 작은 것
    - cost 는 출발지 부터 dest 까지 도달하기 위한 최단 거리
    - dest 도달 불가 or cost > revenue 이면 판매 불가
      즉, 판매 "가능" 상품 중, 우선 순위 높은 1개 판매
      해당 id 출력
      관리 목록에서 제외
      if 판매 가능 상품 없으면 -1 출력하고 상품 제거

    5) 여행 상품 출발지 변경
    - 전부 출발지를 s 로 변경하는 명령어
    - 출발지 변경에 따라 각 상품의 cost 가 변경될 수 있음
    */

    for (int q = 0; q < Q; ++q)
    {
        int cmd;
        cin >> cmd;

        switch (cmd)
        {
        case 100:
        {
            cin >> N;
            cin >> M;
            for (int m = 0; m < M; ++m)
            {
                int city1, city2, weight;
                cin >> city1 >> city2 >> weight;
                if (city1 == city2)
                {
                    weight = 0;
                }
                graph[city1].push_back({ city2, weight });
                graph[city2].push_back({ city1, weight });
            }
            updateCosts();

            // 출력
            // cout << "----------------------" << endl;
            // for (const auto& info : graph)
            // {
            //     cout << info.first << " : ";
            //     for (const auto& nextInfo : info.second)
            //         cout << nextInfo.first << " " << nextInfo.second << " / ";
            // 	cout << endl;
            // }

            break;
        }
        case 200:
        {
            int id, revenue, dest;
            cin >> id >> revenue >> dest;
            products[id] = { id, currentStart, revenue, dest };
            // updateSingleCost(id);
            productQueue.push(products[id]);
            break;
        }
        case 300:
        {
            int id;
            cin >> id;
            if (products.find(id) != products.end())
            {
                products.erase(id);
            }
            break;
        }
        case 400:
        {
            int bestId = findBest();
            cout << bestId << endl;
            break;
        }
        case 500:
        {
            int s;
            cin >> s;
            currentStart = s;
            for (auto& product : products)
            {
                product.second.start = s;
            }
            updateCosts();

            // queue 를 모두 비워주고, 다시 products 내용을 queue 에 넣어준다.
            while (!productQueue.empty())
            {
                productQueue.pop();
            }
            for (auto& product : products)
            {
                productQueue.push(product.second);
            }


            break;
        }
        }
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

// 2) 
