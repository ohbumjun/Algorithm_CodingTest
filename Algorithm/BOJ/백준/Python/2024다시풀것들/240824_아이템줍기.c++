// https://school.programmers.co.kr/learn/courses/30/lessons/87694

// https://codingjj.tistory.com/98
// 자. 사각형 간에 겹치는 부분을 파악하는 것이 어려워 보인다.
// 일단 어디가 겹치는 지를 판단하는 것에 집중하기 보다.
// 일단 각 사각형 외부를 접근 가능한 영역으로 표시한다.
// 그리고 사각형 내부는 모두 0 으로 만들어준다.
// 그러면 자연스럽게 외곽만 남게 된다.
// 또한, 이동 경로 과정에서 더 명확하게 경로 이동을 하기 위해
// 좌표를 2배 뻥튀기 시켜줘야 한다.
#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

typedef struct{
    int y,x;
    int cnt;
}node;


// 별도로 여기서는 최단 거리 정보를 저장하는 배열 x
int board[101][101]; // 좌표 [y , x]
bool visit[101][101];

pair<int,int> dir[] = {{-1,0},{0,1},{1,0},{0,-1}};

bool is_in(int y, int x){
    if(x < 1 || y< 1 || x > 100 || y > 100 || board[y][x] == 0)
        return false;
    return true;
}

int bfs(int ch_x,int ch_y,int itemX,int itemY){

    queue<node> q;
    q.push({ch_y,ch_x,0});
    
    // 여기서 visit 처리 먼저 하는 거 까먹지 말기
    visit[ch_y][ch_x] = true;
    
    while(!q.empty()){
        int y = q.front().y;
        int x = q.front().x;
        int cnt = q.front().cnt;
        q.pop();
        if(x == itemX && y == itemY){
            return cnt/2;
        }
        
        for(int i=0;i<4;i++){
            int dy = dir[i].first;
            int dx = dir[i].second;
            
            if(is_in(y+dy, x+dx) && !visit[y+dy][x+dx]){
                visit[y+dy][x+dx] = true;
                q.push({y+dy,x+dx,cnt+1});
            }
            
        }
    }
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    
    for(int i=0;i<rectangle.size();i++){
        int left_x = rectangle[i][0]* 2, left_y = rectangle[i][1]* 2;
        int right_x = rectangle[i][2] * 2, right_y = rectangle[i][3]* 2;
        
        for(int i= left_x;i <= right_x ; i++){
            board[left_y][i] = 1;
            board[right_y][i] = 1;
        }
        
        for(int i= left_y;i <= right_y ; i++){
            board[i][left_x] = 1;
            board[i][right_x] = 1;
        }
    }
    
    for(int i=0;i<rectangle.size();i++){
        int left_x = rectangle[i][0]* 2, left_y = rectangle[i][1]* 2;
        int right_x = rectangle[i][2]* 2, right_y = rectangle[i][3]* 2;
     
        for(int i=left_y+1 ;i <= right_y -1 ;i++){
            for(int j = left_x+1 ; j<=right_x -1 ;j++){
                board[i][j] = 0;
            }
        }
    }
    
    answer = bfs(characterX* 2,characterY* 2,itemX*2,itemY*2);
    
    return answer;
}