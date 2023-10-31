#include <vector>
#include <iostream>
using namespace std;

int N, M;
int LockRSt, LockCSt; // 해당 값에서부터 검사 시작
int LockREd, LockCEd; // 해당 값 - 1 까지 검사
int totHomNum;


// 자물쇠, 열쇠
// 자물쇠 => N*N
// - 홈
// - 돌기 

// 열쇠 => M*M
// - 홈, 돌기 
// - 회전
// - 이동

// 자물쇠 홈 ~~ 열쇠 돌기 (일치해야 함)
// 자물쇠 돌기 ~~ 열쇠 돌기 (일치 X)
// 자물쇠 홈을 채워서, 비어있는 곳이 없어야 한다.

// 1. 자물쇠 ~ 열쇠 걸치는 모든 영역들에 대해서
// 2. 각 위치에서 회전 경우 모두 조사
// 3. 각각에서 자물쇠 열수 있는지 조사하기

// 시계 방향 90도 회전
void rotate(vector<vector<int>>& originKey)
{
    vector<vector<int>> changedKey;
    changedKey.resize(originKey.size());
    
    for (int i = 0; i < M; ++i)
        changedKey[i].resize(M);
    
    // N : 자물쇠
    // M : 열쇠
    for (int r = 0; r <  M; ++r)
        for (int c = 0; c < M; ++c)
            changedKey[c][M-1-r] = originKey[r][c];
    
    originKey = changedKey;
};

bool IsMatch(int stR, int stC, vector<vector<int>>& Key,
vector<vector<int>> copyLock)
{
    int tmpHomNum = 0;   
    for (int lockR = stR; lockR < stR + M; lockR++)
    {
        for (int lockC = stC; lockC < stC + M; lockC++)
        {
            // 자물쇠의 원래 범위 안에 있어야 한다. (그 외의 범위는 고려 X)
            if (lockR < LockRSt || lockC < LockCSt)
                continue;
            if (lockR >= LockREd || lockC >= LockCEd)
                continue;
            copyLock[lockR][lockC] += Key[lockR - stR][lockC - stC];
        }
    }
    
    // 자물쇠 모든 영역이 1이어야 한다.
    for (int r = LockRSt; r < LockREd; ++r)
    {
        for (int c = LockCSt; c < LockCEd; ++c)
        {
            if (copyLock[r][c] != 1)
                return false;
        }
    }
    
    return true;
}

bool solution(vector<vector<int>> key, vector<vector<int>> originLock) {
    
    N = originLock.size(), M = key.size();
    LockRSt = M - 1, LockCSt = M - 1;
    LockREd = N + M - 1, LockCEd = N + M - 1;
    
    
    // 채워야 하는 홈 개수를 조사한다.
    for (int r = 0; r < N; ++r)
        for (int c = 0; c < N; ++c)
            if (originLock[r][c] == 0)
                totHomNum += 1;
    
    vector<vector<int>> lock;
    lock.resize(N + 2 * (M - 1));
    
    size_t LockRowSize = lock.size();
    
    for (size_t i = 0; i < LockRowSize; ++i)
    {
        lock[i].resize(N + 2 * (M - 1));
        fill(lock[i].begin(), lock[i].end(), 1);
    }
    
    for (int r = 0; r < N; ++r)
        for (int c = 0; c < N; ++c)
            lock[M - 1 + r][M - 1 + c] = originLock[r][c];
    
    
    for (int r = 0; r < N + M; r++)
    {
        for (int c = 0; c < N + M; c++)
        {
             // 4번의 회전
            for (int k = 0; k < 4; ++k)
            {
                rotate(key);
                if (IsMatch(r, c, key, lock)) //
                    return true;
            }
        }
        cout << endl;
    }
    
    
    return false;
}