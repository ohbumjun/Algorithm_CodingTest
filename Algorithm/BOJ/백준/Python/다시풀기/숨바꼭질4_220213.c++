#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <stack>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 100000 + 1
#define INF int(1e9)

using namespace std;

int St, Ed;
std::vector<int> vecDist;
std::vector<bool> vecCheck;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    freopen("input_C.txt", "r", stdin);

    cin >> St;
    cin >> Ed;

    if (Ed < St)
    {
        cout << St - Ed << endl;
        for (int num = St; num >= Ed; num--)
        {
            cout << num << " ";
        }
        exit(0);
    }

    if (Ed == St)
    {
        cout << 0 << endl;
        cout << Ed;
        exit(0);
    }

    // 거리 정보 초기화
    vecDist = std::vector<int>(MAX, INF);
    vecCheck = std::vector<bool>(MAX, false);

    // 경로 정보 세팅
    std::vector<int> vecPath;

    // queue에 들어갈 것
    // 1) 현재 숫자
    // 2) 지금까지 온 횟수
    // 3) 지금까지 온 방법에 대한 내용 (1,2,3 형태로 주어진다)
    std::queue<std::tuple<int, int, std::vector<int>>> Queue;
    std::vector<int> Path;
    Path.reserve(20);
    Queue.push(std::make_tuple(St, 0, Path));

    // 방문 처리
    vecDist[St] = 0;
    vecCheck[St] = true;

    while (!Queue.empty())
    {
	    // Queue에서 꺼낸다.
        std::tuple<int, int, std::vector<int>> Info = Queue.front();
        Queue.pop();

        int CurNum = std::get<0>(Info);
        int CurDist = std::get<1>(Info);
        std::vector<int> CurPath = std::get<2>(Info);

        // minDist 값과 비교
        if (CurDist > vecDist[CurNum])
            continue;

        // 해당 위치에 도달했다면
        if (CurNum == Ed)
        {
            vecPath = CurPath;
        }

        vecDist[CurNum] = CurDist;
        vecCheck[CurNum] = true;

        // 3가지 경우를 모두 간다.
        // 1) 한칸 앞으로
        if (CurNum + 1 < MAX && !vecCheck[CurNum + 1])
        {
            CurPath.push_back(1);
            Queue.push(std::make_tuple(CurNum + 1, CurDist + 1, CurPath));
            CurPath.pop_back();
        }

        // 2) 한칸 뒤로
        if (CurNum -1 >= 0 && !vecCheck[CurNum - 1])
        {
            CurPath.push_back(2);
            Queue.push(std::make_tuple(CurNum - 1, CurDist + 1, CurPath));
            CurPath.pop_back();
        }

        // 3) 순간 이동
        if (CurNum * 2  < MAX && !vecCheck[CurNum * 2])
        {
            CurPath.push_back(3);
            Queue.push(std::make_tuple(CurNum * 2, CurDist + 1, CurPath));
            CurPath.pop_back();
        }
    }

    cout << vecDist[Ed] << endl;

    int Size = vecPath.size();

    int InitEd = Ed;

    std::stack<int> stkPath;

    for (int i = Size - 1; i >= 0; i--)
    {
        if (vecPath[i] == 3)
            Ed /= 2;
        if (vecPath[i] == 2)
            Ed += 1;
        if (vecPath[i] == 1)
            Ed -= 1;
        stkPath.push(Ed);
    }

    while (!stkPath.empty())
    {
        cout << stkPath.top() << " ";
        stkPath.pop();
    }

    cout << InitEd;

    return 0;
}


