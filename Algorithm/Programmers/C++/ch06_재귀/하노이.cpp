// https://programmers.co.kr/learn/courses/13007/lessons/87592

#include <iostream>

using namespace std;

/*
hanoi(n : 옮기는 원소 개수, from : 시작 기둥, to : 목적 기둥, by : 그외 하나 기둥)
{
    if n == 1: from에서 to로 원판 단순히 이동 시키기
    else 
        hanoi(n-1,from,by,to);
        from 에서 to로 원판 이동
        hanoi(n-1,by,to,from);

    - 총 3가지 형태 
    ex) 1) 4개를 움직이는데, 가장 큰 원판을 제외하고, 그외 3개를, by 기둥으로 이동시키기
    ex) 2) 큰 원판을 , 목표 to 기둥으로 이동 시키기
    ex) 3) by에 있는 3개 기둥으로 목표 기둥으로 이동 시키기 
}
*/

void hanoi(int n, int from, int to, int by)
{
    if (n == 1)
    {
        cout << from << " -> " << to << endl;
    }
    else
    {
        hanoi(n - 1, from, by, to);
        cout << from << " -> " << to << endl;
        hanoi(n - 1, by, to, from);
    }
}

int main()
{
    hanoi(2,1,3,2);
    return 0;
}