// https://school.programmers.co.kr/learn/courses/30/lessons/84021

#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
struct Point{
    int row;
    int col;
};

vector<vector<bool> > check;        // 방문 처리
vector<vector<Point> > puzzleList;  // 퍼즐을 담는 리스트
vector<vector<Point> > emptyList;   // 빈 공간을 담는 리스트

// 90도 한번 돌리기
vector<vector<bool>> rotateOnce(vector<vector<bool>> origin){

    int c = origin.size(); // 행
    int r = origin.size(); // 열

    // 반환할 90도 돌아간 보드판
    vector<vector<bool>> board;
    vector<bool> row(r);

    for(int i = 0; i < c; i++) board.push_back(row);

    // 90도 돌리는 작업 (왼쪽으로)
    for(int f = 0; f < origin.size(); f++)
    {
        // f : row
        // s : col
        // ex) 2 x 2 -> origin.size() : 2
        // ex) 0.0 -> 1.0
        // ex) 0.1 -> 0.0
        for(int s = 0; s < origin[f].size(); s++)
        {
            board[origin.size()-s-1][f] = origin[f][s];
        }
    }
    return board;
}

// 다시 방문하지 않도록 빈 공간 메우기
// 퍼즐을 이용하여, 보드판을 채우는 것이다.
// 이때 인자로 들어오는 emptyPoses 은, rePos 를 통해 0.0 으로 맞춰진 것이 아닌
// 원본 좌표 정보가 들어오게 된다.
// emptyPoses 에는 원본 board 에서 0 이었던 부분. 즉, 비어있던 부분들의 좌표 정보가 들어오게 된다.
vector<vector<bool>> fillBoard(vector<Point> emptyPoses, vector<vector<bool> > board)
{
    for(int i = 0; i < emptyPoses.size(); i++){
        int row = emptyPoses[i].row;
        int col = emptyPoses[i].col;
        // 빈칸을 1 으로 만든다. (1 은 채워진 것.)
        board[row][col] = false;
    }
    return board;
}

// 빈공간, 퍼즐 추출하기 (해당 퍼즐을 구분하는 기준은, vector 에 담긴 point 들)
// isPuzzle : puzzle 을 조사하는지 / board 를 조사하는지
vector<Point> getPuzzle(int sRow,int sCol, const vector<vector<bool>>& targetDatas)
{
    int dRow[] = {0,0,-1,1};
    int dCol[] = {-1,1,0,0};
    
    queue<Point> q;
    vector<Point> list;
    check[sRow][sCol] = true;
    Point p = {sRow,sCol};
    q.push(p); 
    list.push_back(p);

    while(!q.empty())
    {
        int curRow = q.front().row;
        int curCol = q.front().col;
        q.pop();
        for(int i = 0; i < 4; i++)
        {
            int nRow = curRow + dRow[i];
            int nCol = curCol + dCol[i];
            
            if(nRow < 0 || nCol < 0 || nRow >= targetDatas.size() || nCol >= targetDatas.size()) continue;
            
            // totPuzzle 이 0 이라면, puzzle 후보가 아닌 것이다
            // puzzle 판에서 1 만 puzzle 요소가 될 수 있다.
            if (check[nRow][nCol]) continue;
            
            if (targetDatas[nRow][nCol] == false) continue;
            
            check[nRow][nCol] = true;
            Point np = {nRow,nCol};
            q.push(np);
            list.push_back(np);
        }
    }
    
    // 전역 변수 puzzleList 안에 vector<Point> 가 들어간다.
    // 공간좌표들을, 2차원 vector 형태로 묶어서 관리한다.
    
    // 해당 퍼즐이 가지고 있는 블록의 좌표들을 모두 반환한다.
    return list;
}

// (0,0)으로 리포지션 시키는 함수
vector<Point> rePos(vector<Point> p){
    int minRow = p[0].row;
    int minCol = p[0].col;

    for(int i = 1; i < p.size(); i++)
    {
        minRow = min(minRow,p[i].row);
        minCol = min(minCol,p[i].col);
    }

    for(int i = 0; i < p.size(); i++)
    {
        p[i].row -= minRow;
        p[i].col -= minCol;
    }
    return p;

}
// 두 퍼즐이 일치하는지 비교하는 함수
int comparePuzzle(vector<Point> a, vector<Point> b){
    int answer = 0;
    
    // rePos 를 이용하여, 모두 왼쪽 상단 좌표가 (0,0) 이 되게끔 맞춰준다.
    a = rePos(a);
    b = rePos(b);

    int count = 0;
    
    // 애초에 개수가 일치하지 않으면 틀림
    if(a.size() != b.size()) return 0;

    for(int i = 0; i < a.size(); i++)
    {
        for(int j = 0; j < b.size(); j++)
        {
            if(a[i].row == b[j].row && a[i].col == b[j].col)
            {
                count++;
                break;
            }
        }
    }
    // 일치하는 좌표의 개수가 같을 때만 맞음
    if(count == a.size()) return a.size();
    else return 0;
}

int solution(vector<vector<int>> game_board, vector<vector<int> > table) {
    // 1) BFS를 통해 퍼즐 맵에서 각각의 퍼즐들의 좌표 정보를 가지고 있는 배열 뭉치를 가져온다
    // 2) 가져온 배열 뭉치의 기준 좌표를 (0,0)으로 통일하여 계산이 가능하도록 치환 작업을 해준다
    // 3) 보드 판의 빈 블록칸을 탐색하며 퍼즐과 칸이 맞는 부분이 있는지 확인한다. 이때 보드판의 빈 블록칸 또한 기준 좌표를 (0,0)으로 만들어주는 작업을 해준다
    // 4) 퍼즐과 칸이 맞는 부분이 있다면 퍼즐 리스트에서 해당 퍼즐을 없애고, 보드판에서 그 자리를 메꿔 더 이상 방문하지 못하도록 한다.
    // 5) 90도를 돌려서 3~4번 과정을 반복한다. 해당 과정은 총 4번이 되거나, 퍼즐이 더 이상 없을 때까지 반복한다
    
    vector<vector<bool> > board;
    vector<vector<bool> > puzzles;
    int tableRow = table.size();
    int tableCol = table[0].size();
    
    for(int i = 0; i < tableRow; i++)
    {
        vector<bool> v1;
        vector<bool> v2;
        vector<bool> v3;
        for(int j = 0; j < tableCol; j++)
        {
            // 원래 board 에서 1은 채워진 공간. 0 은 빈 공간
            // 반면 puzzle 은 1은 puzzle, 0 은 puzzle x
            v1.push_back(!game_board[i][j]);
            v2.push_back(table[i][j]);
            v3.push_back(false);
        }
        board.push_back(v1);
        puzzles.push_back(v2);
        check.push_back(v3);
    }
    
    // 위에까지는 정보를 채워준 초기화 단계

    
    // 자 puzzle 판을 돌면서
    int puzzleRow = puzzles.size();
    int puzzleCol = puzzles[0].size();
    
    for(int f = 0; f < puzzleRow; f++)
        for(int s = 0; s < puzzleCol; s++)
            if(!check[f][s] && puzzles[f][s]) 
                puzzleList.push_back(getPuzzle(f,s,puzzles));
    // if(!check[f][s] && puzzles[f][s]) 에서 
    // !check[f][s] 가 필요한 이유는 getPuzzle 안에서 방문 이후 true 처리하므로
    
    // 회전은 최대 4번만 진행한다.
    int count = 4;
    int answer = 0;
    int boardRow = board.size();
    int boardCol = board.size();
    
    // 자. 이제 다시 본격적으로 방문 로직을 타므로 모든 check 값을 false로
    // 해당 로직은, 매 방문 로직을 마무리할 때마다 다시 reset
    fill(check.begin(),check.end(),vector<bool>(check.size(),false));
    
    while(count--){
        
        // 일단 원본 board 에서 0 들을 empty list 에 넣는다.
        // 
        for(int f = 0; f < boardRow; f++)
            for(int s = 0; s < boardCol; s++)
                if(board[f][s] && !check[f][s]) 
                    emptyList.push_back(getPuzzle(f,s,board));
        
        for(int p = 0; p < puzzleList.size(); p++)
        {
            for(int e = 0; e < emptyList.size(); e++)
            {
                int val = comparePuzzle(puzzleList[p],emptyList[e]);
                if (val == 0) continue;
                answer += val;
                board = fillBoard(emptyList[e],board);
                puzzleList.erase(puzzleList.begin()+p);
                emptyList.erase(emptyList.begin()+e);
                p--;
                break;
            }
        }
        board = rotateOnce(board);

        fill(check.begin(),check.end(),vector<bool>(check.size(),false));
    }
    return answer;
}