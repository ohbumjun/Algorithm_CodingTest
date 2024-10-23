// https://school.programmers.co.kr/learn/courses/30/lessons/42897

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> money) {
    
    // i 를 털면, i - 2 와 i + 2 를 털 수 있다.
    // i 를 털지 않으면 i - 1 와 i + 1 을 털 수 있다.
    // 자. 그런데 원형 dp 라고 생각하지말고, 
    // 그냥 앞에서부터 차례대로 증가하는 방식으로 생각
    // 1) i 를 털면, 
    // i 현재 money + (i-2 를 털었을 때까지의 최대 금액)
    // 2) i 를 털지 않으면, 
    // (i - 1 를 털었을 때까지의 최대 금액)
    
    int answer = 0;
    
    /*
    // dps[idx] : idx 번째 집까지 털엇을 때, 훔칠 수 있는 돈의 최대 액수
    vector<int> dps;
    dps.resize(money.size());
    
    dps[0] = money[0];
    dps[1] = max(money[0], money[1]);
    
    for (int i = 2; i < money.size(); ++i)
    {
        dps[i] = max(money[i] + dps[i - 2], dps[i - 1]);
    }
    
    answer = dps[dps.size() - 1];
    
    그런데 dps[1] 의 값을 저렇게 해도 되는걸까 ?
    money[0] 가 된다는 것은, 1번째 집을 털지 않았다는 것
    money[1] 이 된다는 것은, 1번째 집을 털었다는 것.
    
    그런데 이후의 dps[] 들이 dps[1] 을 참고할 때
    해당 값이 털었다는 것을 의미하는지, 털지 않았다는 것을 의미하는지 모를 수 있지 않을까 ?
    
    즉, 첫번째 집을 터는지, 안터는지에 따라
    dps 배열 값들이 시작부터 달라질 수 있다는 것이다.
    
    따라서 dp 로직을 2번 돌린다고 생각하면 된다.
    */
    
    vector<int> dps;           // idx 를 털었다.
    dps.resize(money.size());
    
    dps[0] = money[0];
    dps[1] = money[0];
    
    for (int i = 2; i < money.size(); ++i)
    {
        // ex) dps[2] -> 여기서는 일단, 무조건 첫집을 턴 케이스만 생각하게 될 것이다.
        dps[i] = max(money[i] + dps[i - 2], dps[i - 1]);
    }
    
    // 자. 여기서 중요한 것은, 첫번째 집을 턴 경우를 고려한 것
    // 다시 말하면, 맨 마지막 집은 첫번째 집과 이웃된 것이고
    // 그래서 마지막 집은 애초에 털지 못함. 따라서 money[money.size() - 2] 가 되어야 함
    // answer = money[money.size() - 1];
    answer = dps[money.size() - 2];
    
    // 자. 이제 처음 집을 털지 않은 경우
    dps[0] = 0;
    dps[1] = money[1];
    
    for (int i = 2; i < money.size(); ++i)
    {
        // ex) dps[2] -> 여기서는 꼭 첫번째 집을 턴 케이스만 고려하지는 않는다.
        dps[i] = max(money[i] + dps[i - 2], dps[i - 1]);
    }
    
    return max(answer, dps[money.size() - 1]);
}