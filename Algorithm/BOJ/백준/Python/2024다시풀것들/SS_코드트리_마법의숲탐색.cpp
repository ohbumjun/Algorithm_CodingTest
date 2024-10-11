// https://www.codetree.ai/training-field/frequent-problems/problems/magical-forest-exploration/description?page=1&pageSize=5

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <cassert>
#include <vector>
#include <string>
#include <cstring>
// #include <climits>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

// #define DEBUG 1

using namespace std;

int R, C, K;

// 열, d
vector<pair<int, int>> GolemStInfo;

// 골렘 출구 방향
vector<int> GolemExitDir;

// 현재 골렘 중앙 위치
// -1, -1 : 골렘 숲에 없음.
vector<pair<int,int>> GolemPos; // 인접 공간 확인할 때 필요하다.

// Map 정보 -> 어떤 골렘이 있는지
// -1 : 아무것도 없음
vector<vector<int>> Map;

// 북, 동, 남, 서
int dRow[]  = { -1, 0, 1, 0 };
int dCol[]  = { 0, 1, 0, -1 };

void Input()
{
    cin >> R >> C >> K;

    Map.resize(R, vector<int>(C, -1));
    GolemStInfo.resize(K);
    GolemPos.resize(K);
    GolemExitDir.resize(K);

    for (int k = 0; k < K; ++k)
    {
        int c, d;
        cin >> c >> d;
        GolemStInfo[k] = { c - 1, d };
        GolemPos[k] = { -1, c - 1 };
    }
}

void rotateExitDir(int golem, bool clock)
{
    int dir = GolemExitDir[golem];
    if (clock) // 시계
    {
        dir = (dir + 1) % 4;
    }
    else
    {
        dir -= 1;
        if (dir < 0)
			dir = 3;
    }
    GolemExitDir[golem] = dir;
}

bool initGolemPos(int row, int col, vector<pair<int, int>>& poses)
{
    poses.clear();

    // 가운데
    poses.push_back({ row, col });
    // 위
    poses.push_back({ row - 1, col });
    // 오른쪽
    poses.push_back({ row, col + 1 });
    // 왼쪽
    poses.push_back({ row, col - 1 });
    // 아래쪽
    poses.push_back({ row + 1, col });

    if (row + 1 >= 0 && Map[row + 1][col] != -1) // 아래 부분에 이미 골렘 있음
        return false;

    return true;
}

bool isOutOfMap(int row, int col)
{
    if (row < 0 || row >= R || col < 0 || col >= C)
		return true;
    for (int d = 0; d < 4; ++d)
    {
        int nxtR = row + dRow[d];
        int nxtC = col + dCol[d];
        if (nxtR < 0 || nxtR >= R || nxtC < 0 || nxtC >= C)
			return true;
    }
	return false;
}

void resetGolems()
{
    for (int r = 0; r < R; ++r)
    {
        for (int c = 0; c < C; ++c)
        {
            if (Map[r][c] == -1)
                continue;
            int golem = Map[r][c];
            GolemPos[golem] = { -1, -1 };
            Map[r][c] = -1;
        }
    }
}

// 범위가 벗어나지 않는 대상들에 대해서만 호출해야 한다.
vector<pair<int, int>> moveSouth(int golem, vector<pair<int, int>>& oldPoses)
{
    vector<pair<int, int>> newPos;
    for (int i = 0; i < oldPoses.size(); ++i)
    {
        int r = oldPoses[i].first;
        int c = oldPoses[i].second;
        int nxtR = r + 1;
        int nxtC = c;
        newPos.push_back({ nxtR, nxtC });
    }

    // 최종 위치에 대해서만 표시해주기
    // for (int i = 0; i < oldPoses.size(); ++i)
    // {
    //     int oldR = oldPoses[i].first;
    //     int oldC = oldPoses[i].second;
    //     Map[oldR][oldC] = -1;
    // 
    //     int newR = newPos[i].first;
    //     int newC = newPos[i].second;
    //     Map[newR][newC] = golem;
    // }

    return newPos;
}
vector<pair<int, int>> moveWest(int golem, vector<pair<int, int>>& oldPoses)
{
    vector<pair<int, int>> newPos;
    for (int i = 0; i < oldPoses.size(); ++i)
    {
		int r = oldPoses[i].first;
		int c = oldPoses[i].second;
		int nxtR = r;
		int nxtC = c - 1;
        newPos.push_back({ nxtR, nxtC });
	}

    // for (int i = 0; i < oldPoses.size(); ++i)
    // {
    //     int oldR = oldPoses[i].first;
    //     int oldC = oldPoses[i].second;
    //     Map[oldR][oldC] = -1;
    // 
    //     int newR = newPos[i].first;
    //     int newC = newPos[i].second;
    //     Map[newR][newC] = golem;
    // }

    return newPos;
}
vector<pair<int, int>> moveEast(int golem, vector<pair<int, int>>& oldPoses)
{
    vector<pair<int, int>> newPos;

    for (int i = 0; i < oldPoses.size(); ++i)
    {
		int r = oldPoses[i].first;
		int c = oldPoses[i].second;
		int nxtR = r;
		int nxtC = c + 1;
        newPos.push_back({ nxtR, nxtC });
	}

    // for (int i = 0; i < oldPoses.size(); ++i)
    // {
    //     int oldR = oldPoses[i].first;
    //     int oldC = oldPoses[i].second;
    //     Map[oldR][oldC] = -1;
    // 
    //     int newR = newPos[i].first;
    //     int newC = newPos[i].second;
    //     Map[newR][newC] = golem;
    // }

    return newPos;
}
bool checkSouth(int golem, const vector<pair<int, int>>& pos)
{
    for (int i = 0; i < pos.size(); ++i)
    {
        int r = pos[i].first;
        int c = pos[i].second;
        int nxtR = r + 1;
        int nxtC = c;

        // if (nxtR < 0 || nxtR >= R || nxtC < 0 || nxtC >= C)
		// 	return false;
        // 맨 위는 여전히 남아있을 수 있다.
        if (nxtR >= R)
            return false;

        if (nxtR >= 0 && nxtR < R && nxtC >= 0 && nxtC < C)
        {
			if (Map[nxtR][nxtC] != -1 && Map[nxtR][nxtC] != golem)
				return false;
		}
        // if (Map[r][c] != -1 && Map[r][c] != golem)
        //     return false;
    }

    return true;
}

// 왼쪽 아래
bool checkWestSouth(int golem, const vector<pair<int, int>>& pos)
{
    vector<pair<int, int>> nextPos;

    // 서쪽 이동
    for (int i = 0; i < pos.size(); ++i)
    {
        int r = pos[i].first;
        int c = pos[i].second;
        int nxtR = r;
        int nxtC = c - 1;

        // if (nxtR < 0 || nxtR >= R || nxtC < 0 || nxtC >= C)
        //     return false;
        if (nxtC < 0)
            return false;

        // if (Map[r][c] != -1 && Map[r][c] != golem)
        //     return false;
        if (nxtR >= 0 && nxtR < R && nxtC >= 0 && nxtC < C)
        {
            if (Map[nxtR][nxtC] != -1 && Map[nxtR][nxtC] != golem)
                return false;
        }

        nextPos.push_back({ nxtR, nxtC });
    }

    // 남쪽 이동
    if (!checkSouth(golem, nextPos))
		return false;

	return true;
}

// 오른쪽 아래
bool checkEastSouth(int golem, const vector<pair<int, int>>& pos)
{
    vector<pair<int, int>> nextPos;

    // 동쪽 이동
    for (int i = 0; i < pos.size(); ++i)
    {
        int r = pos[i].first;
        int c = pos[i].second;
        int nxtR = r;
        int nxtC = c + 1;

        // if (nxtR < 0 || nxtR >= R || nxtC < 0 || nxtC >= C)
        //     return false;
        if (nxtC >= C)
            return false;

        // if (Map[r][c] != -1 && Map[r][c] != golem)
        //     return false;
        if (nxtR >= 0 && nxtR < R && nxtC >= 0 && nxtC < C)
        {
            if (Map[nxtR][nxtC] != -1 && Map[nxtR][nxtC] != golem)
                return false;
        }

        nextPos.push_back({ nxtR, nxtC });
    }

    // 남쪽 이동
    if (!checkSouth(golem, nextPos))
        return false;

    return true;
}

bool isNearBy(int r, int c, int otherR, int otherC)
{
    for (int d = 0; d < 4; ++d)
    {
        int nearR = r + dRow[d];
        int nearC = c + dCol[d];
        if (nearR == otherR && nearC == otherC)
			return true;
    }

    return false;
}

vector<int> getNearbyGolems(int curGolemRow, int curGolemCol, int golem)
{
    vector<int> result;

    for (int i = 0; i < GolemPos.size(); ++i)
    {
        if (i == golem)
            continue;
        if (GolemPos[i].first == -1)
            continue;

        int compGolemRow = GolemPos[i].first;
        int compGolemCol = GolemPos[i].second;

        // 상하좌우 칸도 살펴보고, curGolemRow, curGolemCol 이 인접한지 확인
        for (int d = 0; d < 4; ++d)
        {
            int nxtCompRow = compGolemRow + dRow[d];
            int nxtCompCol = compGolemCol + dCol[d];

            if (isNearBy(curGolemRow, curGolemCol, nxtCompRow, nxtCompCol))
            {
                result.push_back(i);
                break;
            }
        }
    }

    return result;
}

void findNearByExit(int exitRow, int exitCol, int golem, 
    vector<bool>& check, int& lowest)
{
    check[golem] = true;

    // 이 부분에서 재귀적으로 타고 들어가야 한다.
    vector<int> nearBys = getNearbyGolems(
        exitRow, exitCol, golem);

    for (int nearByGolem : nearBys)
    {
        // 해당 golem row + 1 을 확인
        if (check[nearByGolem])
            continue;
        int nearByGolemRow = GolemPos[nearByGolem].first;
        int nearByGolemCol = GolemPos[nearByGolem].second;
        // int nearByGolemSouth = nearByGolemRow + 1; // 골렘 칸 맨 아래
        // lowest = max(lowest, nearByGolemSouth + 1); // 실제 rot + 1
        lowest = max(lowest, nearByGolemRow + 1);
        // nearby golem 의 exit 을 찾는다
        int nearGolemExitDir = GolemExitDir[nearByGolem];
        int nearGolemExitRow = nearByGolemRow + dRow[nearGolemExitDir];
        int nearGolemExitCol = nearByGolemCol + dCol[nearGolemExitDir];
        findNearByExit(nearGolemExitRow, nearGolemExitCol, nearByGolem, check, lowest);
    }
}

void Solve()
{
    // 정령들은, 북에서만 들어올 수 있다.
    // 골렘 5칸
    // - 중앙 제외 4방향 어디서든 탐승 가능
    // - 내릴 때는 정해진 출구로만 내릴 수 있다.

    // 골렘 위치
    // 각 정령의 위치 
    // 골렘 사라짐 여부
    // 정령 끝 여부 ??
    int ans = 0;

    for (int k = 0; k < K; ++k)
    {
        // 골렘 시작
        // - 가장 북쪽 (row = 0), c 열에서 "내려온다"
        // - 초기 출구 방향은 di 에 저장 
        pair<int,int> golemInfo = GolemStInfo[k];
        // curRow, curCol 은, 골렘의 위치이다.
        int curGolemCol = golemInfo.first;

        // 시작 row 를 02로 설정하는 것이 매우 중요하다
        // -1 혹은 0 으로 해도 바로 틀린다.
        int curGolemRow = -2;
        int nxtGolemRow = curGolemRow;
        int nxtGolemCol = curGolemCol;

        int lowest = -1;
        bool outOfMap = false;
        int exitDir = golemInfo.second;
        GolemExitDir[k] = exitDir;

        // 골렘 위치 정보
        vector<pair<int,int>> golemPoses;
        bool result = initGolemPos(curGolemRow, curGolemCol, golemPoses);

        if (!result)
        {
            //   일부 골렘이 이제 내려가려고 하는데 만약 숲을 벗어난 상태라면
            //   현재 골렘과 Map 에 있는 골렘 모두를 비워버린다.
            //   이때 정령이 도달하는 최종 위치를 답에 포함시키지 않는다.
            //   이때 이미 누적된 행 총합은 그대로 둔다.
            // 모든 골렘 정보를 reset 한다.
            resetGolems();
            continue;
        }

        // 정령의 최종 위치를 기록할 때까지 계속 이동
        while (true)
        {
            nxtGolemRow = curGolemRow;
            nxtGolemCol = curGolemCol;

            // 가장 마지막 남단으로 내려간 경우
            if (curGolemRow + 1 >= R - 1)
            {
                lowest = curGolemRow + 1; // 요청은 한칸 더 내려감
                break;
            }

            // 가운데 점을 중심으로 골렘 5칸을 채워준다.
            initGolemPos(nxtGolemRow, nxtGolemCol, golemPoses);

            // 일단 최대한 골렘을 내린다.
            // 골렘 탐색 과정
            // - 1) 남쪽 한칸 내려가기
            //   아래 칸들이 비어있을 때만 내려갈 수 있다 
            if (checkSouth(k, golemPoses))
            {
                golemPoses = moveSouth(k, golemPoses);
                nxtGolemRow += 1;
			}
            else
            {
                // - 2) 만약 1. 이 불가능하다면, 서쪽 + 남쪽 으로 이동
                //   이 경우, 출구가 반시계 방향 회전. 
                if (checkWestSouth(k, golemPoses))
                {
                    golemPoses = moveWest(k, golemPoses);
                    golemPoses = moveSouth(k, golemPoses);
                    nxtGolemRow += 1;
                    nxtGolemCol -= 1;
                    rotateExitDir(k, false);
                }
                else
                {
                    if (checkEastSouth(k, golemPoses))
                    {
                        // - 3) 1.2 가 불가능하다면, 동쪽 + 남쪽
                        //   1.2 와 마찬가지로 범위 검사
                        //   이 경우, 출구가 "시계" 방향 회전
                        golemPoses = moveWest(k, golemPoses);
                        golemPoses = moveSouth(k, golemPoses);
                        nxtGolemRow += 1;
                        nxtGolemCol += 1;
                        rotateExitDir(k, true);
                    }
                    else
                    {
                        //   일부 골렘이 이제 내려가려고 하는데 만약 숲을 벗어난 상태라면
                        //   현재 골렘과 Map 에 있는 골렘 모두를 비워버린다.
                        //   이때 정령이 도달하는 최종 위치를 답에 포함시키지 않는다.
                        //   이때 이미 누적된 행 총합은 그대로 둔다.
                        // 일부가 Map 에서 벗어났는지 확인하기.
                        if (isOutOfMap(curGolemRow, curGolemCol))
                        {
                            // 모든 골렘 reset
                            resetGolems();
                            outOfMap = true;
                            break;
                        }

                        // 여기로 들어오면, 더이상 내려갈 공간이 없음.
                        // 일단, 아래칸으로 한번 내려가보기.
                        lowest = max(lowest, curGolemRow + 1);

                        // - 4) 만약 가장 남단이라서, 이동 불가능하다면
                        //   정령이, 골렘 내 상하좌우 인접 칸으로 이동 가능
                        //   현재 골렘 출구가, 다른 골렘의 5칸과 "인접"하다면, 해당 출구를 통해
                        //   다른 골렘으로 이동 가능.
                        //   "인접" 이다. 겹치는 것 아니다.
                        // 단 중요한 것은, "출구" 근처의 인접 공간 찾기
                        int curExitDir = GolemExitDir[k];
                        int exitRow = curGolemRow + dRow[curExitDir];
                        int exitCol = curGolemCol + dCol[curExitDir];
                        
                        vector<bool> check(K, false);
                        findNearByExit(exitRow, exitCol, k, check, lowest);

                        // // 이 부분에서 재귀적으로 타고 들어가야 한다.
                        // vector<int> nearBys = getNearbyGolems(
                        //     exitRow, exitCol, k);
                        // 
                        // for (int nearByGolem : nearBys)
                        // {
                        //     // 해당 golem row + 1 을 확인
                        //     int nearByGolemRow = GolemPos[nearByGolem].first;
                        //     lowest = max(lowest, nearByGolemRow + 1);
                        // }

                        break; // while 문에서 벗어난다.
                    }
                }
            }

            curGolemRow = nxtGolemRow;
            curGolemCol = nxtGolemCol;
        }

        // 최종 위치 기록
        if (outOfMap == false)
        {
            GolemPos[k] = { curGolemRow, curGolemCol };
            int finalExitDir = GolemExitDir[k];
            ans += lowest + 1;
            assert(lowest != -1);

            // 현재 위치에 기록하기
            initGolemPos(curGolemRow, curGolemCol, golemPoses);
            for (int i = 0; i < golemPoses.size(); ++i)
            {
				int r = golemPoses[i].first;
				int c = golemPoses[i].second;
				Map[r][c] = k;
			}

            bool debug = false;
        }
        else
        {
            bool out = true;
        }
    }

    cout << ans << endl;
}


int main() {
	ios::sync_with_stdio(false);

	cin.tie(NULL);
	cout.tie(NULL);

	// freopen("input_c.txt", "r", stdin);

	Input();

	Solve();

	return 0;
}


