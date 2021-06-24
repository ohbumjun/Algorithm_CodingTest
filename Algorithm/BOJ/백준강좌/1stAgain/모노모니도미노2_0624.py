# https://www.acmicpc.net/problem/20061

def simulate(board, col, what):
    # what = type (C++, Java)
    # what = 1 1x1, 2 = garo (col, col+1), 3 = sero
    ans = 0
    max_row = -1
    for i in range(len(board)):
        if board[i][col] == 0:
            max_row = i
        else:
            break
    if what == 2:
        max_row_2 = -1
        for i in range(len(board)):
            if board[i][col+1] == 0:
                max_row_2 = i
            else:
                break
        max_row = min(max_row, max_row_2)
    board[max_row][col] = 1
    if what == 2:
        board[max_row][col+1] = 1
    if what == 3:
        board[max_row-1][col] = 1
    deleted_row = -1
    for i in range(len(board)):
        ok = True  # ok = all (C++, Java)
        for j in range(len(board[i])):
            if board[i][j] == 0:
                ok = False
        if ok:
            if deleted_row < i:
                deleted_row = i
            ans += 1
    if ans > 0:
        for i in range(deleted_row, -1, -1):
            for j in range(len(board[i])):
                board[i][j] = 0
                if i - ans >= 0:
                    board[i][j] = board[i-ans][j]
    cnt = 0
    for i in range(0, 2):
        exists = False
        for j in range(len(board[i])):
            if board[i][j] != 0:
                exists = True
        if exists:
            cnt += 1
    if cnt > 0:
        bn = len(board)
        for i in range(bn-1, -1, -1):
            for j in range(len(board[i])):
                board[i][j] = 0
                if i - cnt >= 0:
                    board[i][j] = board[i-cnt][j]

    return ans


n = int(input())
ans = 0
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
for _ in range(n):
    t, x, y = map(int, input().split())
    if t == 1:
        ans += simulate(green, y, 1)
    elif t == 2:
        ans += simulate(green, y, 2)
    elif t == 3:
        ans += simulate(green, y, 3)
    if t == 1:
        ans += simulate(blue, x, 1)
    elif t == 2:
        ans += simulate(blue, x, 3)
    elif t == 3:
        ans += simulate(blue, x, 2)

print(ans)
cnt = 0
for i in range(len(green)):
    for j in range(len(green[i])):
        if green[i][j] > 0:
            cnt += 1
for i in range(len(blue)):
    for j in range(len(blue[i])):
        if blue[i][j] > 0:
            cnt += 1
print(cnt)


'''
C++

#include <iostream>
#include <cassert>
#include <vector>
using namespace std;
// col : 해당 블록이 놓인 위치
// type : 어떤 유형의 블록인가 
int simulate(vector<vector<int>> &board, int col, int type) {
    // type = 1 1x1, 2 = garo (col, col+1), 3 = sero
    int ans = 0;
    int max_row = -1;

    // 해당 블록이 어디까지 내려갈 수 있는지를 구하는 문제이다 
    for (int i=0; i<board.size(); i++) {
        if (board[i][col] == 0) {
            max_row = i;
        } else {
            break;
        }
    }

    // 가로 블록의 경우 
    // 오른쪽 요소도 어디까지 가는지를 구해야 한다 
    if (type == 2) {
        int max_row_2 = -1;
        for (int i=0; i<board.size(); i++) {
            if (board[i][col+1] == 0) {
                max_row_2 = i;
            } else {
                break;
            }
        }
        max_row = min(max_row, max_row_2);
    }

    // 일단 블록을 놓고 
    board[max_row][col] = 1;
    if (type == 2) board[max_row][col+1] = 1; // 가로 : 오른쪽에 요소 배치
    if (type == 3) board[max_row-1][col] = 1; // 세로 : 위쪽에 요소 배치 

    // 이제부터는 블록을 지울 것이다 
    int deleted_row = -1;
    for (int i=0; i<board.size(); i++) {
        bool all = true;
        for (int j=0; j<board[i].size(); j++) {
            // 빈칸이 있다면, 해당 행이 모두 차있는 것이 아니기 때문에 false 처리해준다 
            if (board[i][j] == 0) {
                all = false;
            }
        }
        if (all) {
            if (deleted_row < i) {
                // 지워지는 행 기록 
                // 위에서부터 내려오기 때문에
                // 결과적으로 deleted_row에 저장되는 행은
                // 지워지는 행 중 가장 아래에 있는 행이 된다 
                deleted_row = i;
            }
            // 정답에 1 더해주기 
            // 왜냐하면, 해당 세트를 하나 지울때마다 점수가 1 증가한다고 했기 때문이다 
            ans += 1;
            // 해당 열을 모두 지워준다 
            for (int j=0; j<board[i].size(); j++) {
                board[i][j] = 0;
            }
        }
    }
    // 만약 지워진 행이 존재한다면  
    // ans : 현재 지워진 행의 개수 
    if (ans > 0) {
        // 지워주고, 쭉 내려주기 
        for (int i=deleted_row; i>=0; i--) {
            for (int j=0; j<board[i].size(); j++) {
                board[i][j] = 0;
                if (i-ans >= 0) {
                    // 현재 지워진 행의 수만큼 아래로 내리기 
                    // 이게 그런데 연속적으로 행이 지워질 수가 있나 ? 
                    // ㅇㅇㅇ ... 세로 2칸짜리가 아래로 쭉 내려가는 경우가 있으니 
                    board[i][j] = board[i-ans][j];
                }
            }
        }
    }

    // 자. 이제 블록은 다 지웠다
    // 이번에는 연한 부분을 살펴볼 것이다
    // 우선 연한부분을 보면서, 블록이 있는지 없는지
    // 존재유무 만을 살펴볼 것이다 
    int cnt = 0;
    for (int i=0; i<2; i++) {
        bool exists = false;
        for (int j=0; j<board[i].size(); j++) {
            if (board[i][j] != 0) {
                exists = true;
            }
        }
        // 해당 행이 존재하면 + 1
        // 아니 그런데 왜 행 단위로 조사하는 거지 ?
        // 블록 단위가 아니라 ?
        // 왜냐하면, 어차피 행 단위로 지워줄 것이기 때문이다 
        // ex) 2개의 행에 존재한다 ? 그러면 2개 행만큼 내려주면 되는 것이기 때문이다 
        if (exists) cnt += 1;
    }

    // 아래는 실제 내려주는 코드이다 
    if (cnt > 0) {
        // 아래서부터 위로 올라오면서 지워줄 것이다 
        int bn = board.size();
        for (int i=bn-1; i>=0; i--) {
            for (int j=0; j< board[i].size(); j++) {
                board[i][j] = 0;
                if (i-cnt >= 0) {
                    board[i][j] = board[i-cnt][j];
                }
            }
        }
    }
    return ans;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    int ans = 0;

    // green, blue 2가지 배열이 존재한다고 해보자 
    // 크기가 같은 이유는, 우리가 blue도 아래방향으로 대칭시켜놨기 때문이다 

    vector<vector<int>> green(6, vector<int>(4));
    vector<vector<int>> blue(6, vector<int>(4));
    while (n--) {
        int t, x, y; // 블록 번호, 행, 열 
        // 이제 blue를 대칭이동시켰기 때문에, 사실 행은 별로 의미없을 수도 있다 
        // 어차피 아래로 내리는 방향만 고려할 것이기 때문에
        // (1,1) 에 놓나 vs (1,2) 에 놓나. 별 차이가 없어지기 때문이다 
        cin >> t >> x >> y;

        // 초록색 처리 
        if (t == 1) {
            // simulate : 블록을 배치하는 것 
            ans += simulate(green, y, 1);
        } else if (t == 2) {
            ans += simulate(green, y, 2);
        } else if (t == 3) {
            ans += simulate(green, y, 3);
        }

        // 파란색 처리 
        if (t == 1) {
            // 여기서 특별한 점은 y가 아니라 x를 넣는다는 것이다
            // 이동시키는 motion을 처리해주기 위해서 x를 사용하는 것이고
            // 초록색 이동시에는 y를 사용하는 것이다 
            ans += simulate(blue, x, 1);
        } else if (t == 2) {
            ans += simulate(blue, x, 3);
        } else if (t == 3) {
            ans += simulate(blue, x, 2);
        }
    }
    cout << ans << '\n';
    int cnt = 0;
    for (int i=0; i<green.size(); i++) {
        for (int j=0; j<green[i].size(); j++) {
            if (green[i][j] > 0) cnt += 1;
        }
    }
    for (int i=0; i<blue.size(); i++) {
        for (int j=0; j<blue[i].size(); j++) {
            if (blue[i][j] > 0) cnt += 1;
        }
    }
    cout << cnt << '\n';
    return 0;
}

'''
