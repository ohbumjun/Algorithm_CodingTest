// https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=2&pageSize=5

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

int N,M,K;

// 상하좌우
int dRow[] = {-1, 1, 0,0};
int dCol[] = {0,0,-1,1};

// 빈칸 : 이동 가능 (0의 값)
// 벽 : (1 ~ 9 의 값)
// - 이동 불가
// - 1 ~ 9 내구도
// - 회전할 때 1씩 내구도 감소
// - 내구도 0 이되면 "빈칸" 이 된다.
// 출구
// - 참가자가 도달하면 탈출
vector<vector<int>> miros;
vector<vector<vector<int>>> partMap;
vector<pair<int,int>> partPoses;
vector<int> partMoved;
int outRow, outCol;
vector<bool> isOut;

// 시계 방향 90도 회전
void rotate(int stR, int stC, int height, int width)
{
	// 2 x 3 => 3 x 2
	// 0.0 -> 0.2
	// 2.0 -> 0.0
	// 0.1 -> 1.1

	vector<vector<int>> tempRot(width, vector<int>(height, 0));

	// 출발점 0,0 으로 조정한다.
	vector<vector<int>> revised(height, vector<int>(width, 0));

	for (int r = stR; r < stR + height; ++r)
	{
		for (int c = stC; c < stC + width; ++c)
		{
			int accessRow = r - stR;
			int accessCol = c - stC;

			revised[accessRow][accessCol] = miros[r][c];
		}
	}
		
	// idx, newR, newC
	vector<tuple<int, int, int>> newMoved;
	int movedOutRow = -1, movedOutCol = -1;

	for (int r = 0; r < height; ++r)
	{
		for (int c = 0; c < width; ++c)
		{
			int rotRow = c;
			int rotCol = height - 1 - r;

			rotRow += stR;
			rotCol += stC;

			int realRow = r + stR;
			int realCol = c + stC;

			// 출구 회전
			if (outRow == realRow && outCol == realCol)
			{
				movedOutRow = rotRow;
				movedOutCol = rotCol;
			}

			// 참가자들 회전
			for (int i = 0; i < M; ++i)
			{
				int partRow = partPoses[i].first;
				int partCol = partPoses[i].second;

				// 이미 탈출 참가자 고려 X
				if (isOut[i])
					continue;

				if (partRow == realRow && partCol == realCol)
				{
					newMoved.push_back({ i, rotRow, rotCol });
				}
			}

			// 벽 내구도 감소
			if (revised[r][c] > 0)
				revised[r][c] -= 1;

			tempRot[rotRow - stR][rotCol - stC] = revised[r][c];
		}
	}

	// 회전 출구 적용
	outRow = movedOutRow;
	outCol = movedOutCol;

	// 참가자 회전 적용
	for (int idx = 0; idx < newMoved.size(); ++idx)
	{
		int parti, newR, newC;
		tie(parti, newR, newC) = newMoved[idx];

		int partRow = partPoses[parti].first;
		int partCol = partPoses[parti].second;

		partPoses[parti] = { newR, newC };

		// 기존 위치에서 지우기
		auto iter = std::find(partMap[partRow][partCol].begin(),
			partMap[partRow][partCol].end(), parti);

		assert(iter != partMap[partRow][partCol].end());

		int findIdx = distance(partMap[partRow][partCol].begin(),
			iter);
		partMap[partRow][partCol].erase(
			partMap[partRow][partCol].begin() + findIdx);

		// 새로운 위치에 추가하기
		partMap[newR][newC].push_back(parti);
		
	}

	for (int r = 0; r < height; ++r)
	{
		for (int c = 0; c < width; ++c)
		{
			miros[stR + r][stC + c] = tempRot[r][c];
		}
	}
}

void Input()
{


	cin >> N >> M >> K;

	miros.resize(N, vector<int>(N, 0));
	partMap.resize(N, vector<vector<int>>(N));

	for (int r = 0; r < N; ++r)
		for (int c = 0; c < N; ++c)
			cin >> miros[r][c];

	partMoved.resize(M);
	partPoses.resize(M);
	isOut.resize(M, false);

	for (int m = 0; m < M; ++m)
	{
		int r, c;
		cin >> r >> c;
		r -= 1;
		c -= 1;
		partPoses[m] = { r,c };
		partMap[r][c].push_back(m);
	}

	cin >> outRow >> outCol;
	outRow -= 1;
	outCol -= 1;
}

bool check(int stR, int stC, int edR, int edC)
{
	bool isOutExist = false;
	bool isPartiExist = false;
	for (int r = stR; r <= edR; ++r)
	{
		for (int c = stC; c <= edC; ++c)
		{
			if (r == outRow && c == outCol)
				isOutExist = true;
			for (int m = 0; m < M; ++m)
			{
				int partiR = partPoses[m].first;
				int partiC = partPoses[m].second;

				// 이미 탈출한 참가자 제외
				if (isOut[m])
					continue;

				if (r == partiR && c == partiC)
					isPartiExist = true;
			}
		}
	}

	return isOutExist && isPartiExist;
}

void Solve()
{

	// K 초 반복
	// - 모든 참가자 중간에 탈출했다면 게임 X
	for (int k = 0; k < K; ++k)
	{
		int allOut = true;

		for (int m = 0; m < M; ++m)
		{
			if (isOut[m] == false)
			{
				allOut = false;
				break;
			}
		}

		if (allOut)
			break;

		// >> 참가자 이동
		// 1초마다, "모든" 참가자 "한칸" 이동
		// 거리 : abs() + abs()
		// 모든 참가자 "동시에" 움직임
		// 상하 좌우
		// 벽 이동 X
		// 이동칸은, 기존칸보다 "출구" 까지의 거리가 가까워야 한다.
		// 이동 가능칸이 2개 이상 -> 상하로 먼저
		// 움직일 수 없으면 이동 X
		// 한칸에 2명 이상 존재 가능

		// 참가자, r, c
		vector<tuple<int, int, int>> newMoved; 

		for (int m = 0; m < M; ++m)
		{
			// 현재위치 ~ 출구
			int partRow = partPoses[m].first;
			int partCol = partPoses[m].second;

			// 이미 탈출한 참가자는 고려 X
			if (isOut[m])
				continue;

			vector<int> moveDirs;
			int minDist = abs(partRow - outRow) + abs(partCol - outCol);
			
			for (int d = 0; d < 4; ++d)
			{
				int nxtRow = partRow + dRow[d];
				int nxtCol = partCol + dCol[d];

				// 범위 out X
				if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
					continue;

				// 벽 X
				if (miros[nxtRow][nxtCol] > 0)
					continue;

				int nxtDist = abs(nxtRow - outRow) + abs(nxtCol - outCol);

				if (nxtDist < minDist)
				{
					moveDirs.clear();
					moveDirs.push_back(d);
					minDist = nxtDist;
				}
				else if (nxtDist == minDist)
				{
					// 상.하 움직이는 것 먼저
					int oldD = moveDirs[0];
					if (oldD > d)
					{
						moveDirs.clear();
						moveDirs.push_back(d);
					}
				}
			}

			if (moveDirs.size() == 0)
				continue;

			int moveDir = moveDirs[0];
			int nxtRow = partRow + dRow[moveDir];
			int nxtCol = partCol + dCol[moveDir];

			partMoved[m] += 1;

			newMoved.push_back({ m, nxtRow, nxtCol });
		}

		for (int idx = 0; idx < newMoved.size(); ++idx)
		{
			int parti, newR, newC;
			tie(parti, newR, newC) = newMoved[idx];

			int oldRow = partPoses[parti].first;
			int oldCol = partPoses[parti].second;

			// 기존 위치에서 지워주기
			auto findResult = std::find(partMap[oldRow][oldCol].begin(),
				partMap[oldRow][oldCol].end(), parti);

			assert(findResult != partMap[oldRow][oldCol].end());

			int findIdx = distance(partMap[oldRow][oldCol].begin(), findResult);

			partMap[oldRow][oldCol].erase(partMap[oldRow][oldCol].begin() + findIdx);

			partPoses[parti] = { newR, newC };

			// 출구에 도착했는지 확인하기
			if (newR == outRow && newC == outCol)
			{
				// 도착한 경우는 map 에 추가  X
				isOut[parti] = true;
			}
			else
			{
				// 도착하지 않은 경우만 map 에 추가
				partMap[newR][newC].push_back(parti);
			}
		}

		// 이동 이후, 출구로 나간 탈락자들이 생기므로 한번 더 검사
		allOut = true;

		for (int m = 0; m < M; ++m)
		{
			if (isOut[m] == false)
			{
				allOut = false;
				break;
			}
		}

		if (allOut)
			break;

		// >> 미로 회전
		// 한명이상 참가자. (2명도 가능) ~ 출구. 범위의
		// "가장 작은" "정사각형" 잡기
		// 2개 이상이면, 행 작은 것. 행 같은면 열 작은 것
		// 해당 정사각형 "시계" 방향 "90도" 회전
		// 회전된 "벽" 은 내구도 "1" 감소
		int minRectSize = INT_MAX;
		vector<pair<int, int>> targetPoses;

		// size 2 부터 시작하여 최소 정사각형 찾기
		for (int size = 2; size < N; ++size)
		{
			// 행 작, 열 작.
			for (int r = 0; r <= N - size; ++r)
			{
				for (int c = 0; c <= N - size; ++c)
				{
					// 해당 위치부터 시작하여 
					// 출구와, 참가자를 포함하는 정사각형 찾기
					int stRow = r;
					int stCol = c;
					int edRow = r + size - 1;
					int edCol = c + size - 1;

					// 범위 벗어나면 조사 X
					if (stRow < 0 || stRow >= N || stCol < 0 || stCol >= N)
						continue;

					if (edRow < 0 || edRow >= N || edCol < 0 || edCol >= N)
						continue;

					if (check(stRow, stCol, edRow, edCol))
					{
						minRectSize = size;
						targetPoses.push_back({ stRow, stCol });

						// 가장 작은 size 부터 찾기 때문에 바로 break
						break;
					}
				}
				if (minRectSize != INT_MAX)
					break;
			}
			if (minRectSize != INT_MAX)
				break;
		}

		// 행 작, 열 작 으로 sort (마지막을 선택
		// sort(targetPoses.begin(), targetPoses.end());

		int targetRow = targetPoses.back().first;
		int targetCol = targetPoses.back().second;

		int stRow = targetRow < outRow ? targetRow : outRow;
		int stCol = targetCol < outCol ? targetCol : outCol;

		rotate(stRow, stCol, minRectSize, minRectSize);

		// 회전 이후, 벽 조사해서 내구성 감소시키기 (rotate 안에서 진행)

		// 마지막
		// 모든 참가자들의 "이동 거리 합" 과
		// "출구 좌표" 출력하기
	}
	
	int ans = 0;

	for (int m = 0; m < M; ++m)
		ans += partMoved[m];
	
	cout << ans << endl;
	cout << outRow + 1 << " " << outCol + 1 << endl;
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


// Answer 

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

int N, M, P, C, D;

// 점수
vector<int> scores;
// 탈락 여부
vector<bool> alive;
// 기절 타임 (turn 수로 지정)
vector<int> stun;
// 위치
vector<pair<int, int>> poses;
// 루돌프 위치
int roudRow, roudCol;
// 위치 2차원 벡터
vector<vector<int>> board;
// 상우하좌
int dRow[] = { -1, 0, 1, 0 };
int dCol[] = { 0, 1, 0, -1 };

int getOptDir(int dir)
{
	if (dir == 0)
		return 2;
	else if (dir == 1)
		return 3;
	else if (dir == 2)
		return 0;
	else if (dir == 3)
		return 1;
}

void Input()
{
	cin >> N >> M >> P >> C >> D;

	cin >> roudRow >> roudCol;
	roudRow -= 1;
	roudCol -= 1;

	// - 1은 아무것도 X
	// 0 이상부터 산타
	board.resize(N, vector<int>(N, -1));

	scores.resize(P, 0);
	alive.resize(P, true);
	stun.resize(P, 0);
	poses.resize(P);

	for (int p = 0; p < P; ++p)
	{
		int n, r, c;
		cin >> n >> r >> c;
		n -= 1;
		r -= 1;
		c -= 1;
		poses[n] = { r, c };
		board[r][c] = n;
	}
}

void moveSanta(int santa, int row, int col, int rowDir, int colDir, int moveCnt)
{
	//row,col 에 있는 santa 를 rowDir, colDir 방향으로 moveCnt 만큼 이동시킴
	queue<tuple<int, int, int, int>> q;
	q.push({ santa, row, col, moveCnt });

	while (!q.empty())
	{
		int santa, curRow, curCol, curMoveCnt;
		tie(santa, curRow, curCol, curMoveCnt) = q.front();
		q.pop();

		int nxtRow = curRow + rowDir * curMoveCnt;
		int nxtCol = curCol + colDir * curMoveCnt;

		// 범위를 벗어난다면
		if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
		{
			// 해당 산타 탈락 처리하고
			// 바로 return
			alive[santa] = false;
			return;
		}
		else
		{
			// 범위를 벗어나지 않는다면
			// 1) 해당 위치에 산타가 있다면
			if (board[nxtRow][nxtCol] != -1)
			{
				int oldSanta = board[nxtRow][nxtCol];
				q.push({oldSanta, nxtRow, nxtCol, 1});

				// 새로운 산타로 세팅
				board[nxtRow][nxtCol] = santa;
				poses[santa] = { nxtRow, nxtCol };
			}
			else
			{
				// 2) 산타가 없다면
				// 새로운 위치로 이동 처리하고 return
				board[nxtRow][nxtCol] = santa;
				poses[santa] = { nxtRow, nxtCol };
				return;
			}
		}

	}
}

void Solve()
{
	/*
	1) 게임판 구성
	총 M 번의 턴
	- 매 턴마다 루돌프, 산타 움직임
	- 루돌프 1번. 이후 산타 1 ~ P 차례대로 이동
	  - 기절 혹은 탈락 산타는 이동 X
	- 거리 계산 : (r - r)^2 + (c - c)^2
	*/
	for (int turn = 0; turn < M; ++turn)
	{
		/*
		2) 루돌프 움직임
		- 가장 가까운 산타 1칸 돌진
		- 대신, 탈락하지 않은 산타여야 한다.
		- 가까운 산타 2명 이상 (행큰, 열큰)
		- 8방향 이동 가능
		4) 루돌프에 의한 충돌
		  - 산타 + C 점수
		  - 산타는 루돌프가 이동해온 방향 C 칸 이동
		  - 밀려난 위치 게임 밖 -> 탈락
		  - 밀려난 칸에 다른 산타 ? 상호작용
		  - 산타 기절, 2 턴 이후부터 이동 가능
		*/
		int minDist = INT_MAX;
		vector<pair<int,int>> minSantaInfos;

		for (int p = 0; p < P; ++p)
		{
			if (alive[p] == false)
				continue;
			
			//if (stun[p] > turn) 기절도 충돌 대상
			//	continue;

			int santaRow	= poses[p].first;
			int santaCol	= poses[p].second;
			int curDist		= (roudRow - santaRow) * (roudRow - santaRow) + 
				(roudCol - santaCol) * (roudCol - santaCol);

			if (minDist > curDist)
			{
				minDist = curDist;
				minSantaInfos.clear();
				minSantaInfos.push_back({ santaRow , santaCol});
			}
			else if (minDist == curDist)
			{
				minSantaInfos.push_back({ santaRow , santaCol});
			}
		}
		
		// 행큰, 얼큰
		sort(minSantaInfos.begin(), minSantaInfos.end());

		const pair<int,int>& minSantaPos = minSantaInfos[minSantaInfos.size() - 1];
		int minSantaRow = minSantaPos.first;
		int minSantaCol = minSantaPos.second;
		int minSanta = board[minSantaRow][minSantaCol];

		int rouMovR = 0, rouMovC = 0;

		if (roudRow < minSantaRow)
			rouMovR = 1;
		else if (roudRow > minSantaRow)
			rouMovR = -1;

		if (roudCol < minSantaCol)
			rouMovC = 1;
		else if (roudCol > minSantaCol)
			rouMovC = -1;

		roudRow += rouMovR;
		roudCol += rouMovC;

		// 루돌프에 의한 충돌
		if (board[roudRow][roudCol] != -1)
		{
			int collideSanta = board[roudRow][roudCol];

			// 점수
			scores[collideSanta] += C;

			// 기절 처리
			stun[collideSanta] = turn + 2;

			// 산타 기존 위치 update
			board[roudRow][roudCol] = -1;

			// 안에서 새로운 산타 위치 정보 세팅해줄 것이다.
			moveSanta(collideSanta, 
				roudRow, roudCol, rouMovR, rouMovC, C);
		}
		else
		{
			// 별다른 조치 X
		}

		/*
		3) 산타 움직임
		- 1 ~ P 번까지 "순서대로" 이동
		- 기절 or 탈락 X
		- 루돌프에게 가까워지는 방향으로 1칸
		- 다른 산타 있는 칸. 혹은 게임밖 X
		- 움직일 수 있는 칸이 있더라도, 루돌프와 더 가까워지지 않으면 X
		- 상우하좌 우선순위 이동
		 5) 산타에 의한 충돌
		  - D 점 획득
		  - 이동 방향 반대로 D 칸 이동
		  - 마찬가지로 밀려난 위치 게임 밖 ? -> 탈락
		  - 밀려난 칸에 다른 산타 ? 상호작용
		  - 산타 기절, 2 턴 이후부터 이동 가능
		*/
		for (int p = 0; p < P; ++p)
		{
			if (alive[p] == false)
				continue;
			if (stun[p] > turn)
				continue;
			int stRow = poses[p].first;
			int stCol = poses[p].second;
			int distToRou = (stRow - roudRow) * (stRow - roudRow)
				+ (stCol - roudCol) * (stCol - roudCol);
			int moveDir = -1;
			for (int d = 0; d < 4; ++d)
			{
				int nxtRow = stRow + dRow[d];
				int nxtCol = stCol + dCol[d];
				// 범위 밖
				if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
					continue;
				// 다른 산타 X
				int info = board[nxtRow][nxtCol];
				assert(info != p);
				if (info != -1)
					continue;
				int nxtDist = (nxtRow - roudRow) * (nxtRow - roudRow)
					+ (nxtCol - roudCol) * (nxtCol - roudCol);
				if (distToRou > nxtDist)
				{
					distToRou = nxtDist;
					moveDir = d;
				}
			}
			if (moveDir == -1)
				continue;
			// 이동 처리
			int moveRow = stRow + dRow[moveDir];
			int moveCol = stCol + dCol[moveDir];
			// 기존 위치 X
			board[stRow][stCol] = -1;
			// 루돌프 충돌 여부 확인하기
			if (moveRow == roudRow && moveCol == roudCol)
			{
				// -D 점 획득
				scores[p] += D;

				// - 산타 기절, 2 턴 이후부터 이동 가능
				stun[p] = turn + 2;

				moveDir = getOptDir(moveDir);

				// 산타 이동 처리 (moveSanta 내부에서 사용)
				// board[moveRow][moveCol] = p;

				// - 이동 방향 "반대로" D 칸 이동
				// - 마찬가지로 밀려난 위치 게임 밖 ? ->탈락
				// - 밀려난 칸에 다른 산타 ? 상호작용
				moveSanta(p, roudRow, roudCol, dRow[moveDir], dCol[moveDir], D);
			}
			else
			{
				// 위치 정보 update
				board[moveRow][moveCol] = p;
				poses[p] = { moveRow, moveCol };
			}
		}

		/*
		7) 게임 종료
		P 명 산타 모두 탈락시 게임 종료
		매턴 마자, 아직 탈락 X 산타는 점수 + 1
		*/
		bool allDead = true;
		for (int p = 0; p < P; ++p)
		{
			if (alive[p])
			{
				allDead = false;
				break;
			}
		}

		if (allDead)
			break;

		for (int p = 0; p < P; ++p)
		{
			if (alive[p] == false)
				continue;
			scores[p] += 1;
		}
	}

	// 각 산타가 얻은 최종 점수 출력
	for (int p = 0; p < P; ++p)
	{
		cout << scores[p] << " ";
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


