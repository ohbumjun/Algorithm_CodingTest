// 1번째 풀이 : 완전탐색 + Sliding Window -> 시간초과
#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <set>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> gems) {
    
    vector<int> answer;
    
    // 1) 총 몇개의 보석들이 진열되어 있는지 판단 -> unordered map 에 false 로 세팅
    // 2) 해당 숫자 만큼 Sliding Window 실행
    // 3) 해당 Window 숫자 안에서 Unique 한 값 개수 추가
    // 4) 이동할 때마다, 이전것 제거 + 다음 것 추가 하는 로직 세팅
    
    int TotUniqNum = 0;
    int curUniqN = 0;
    queue<string> qWindow;
    unordered_map<string, int> mapInclude;
    set<string> setGem;
    
    size_t gemSize = gems.size();
    
    for (size_t i = 0; i < gemSize; ++i)
        setGem.insert(gems[i]);
    
    TotUniqNum = setGem.size();
    
    for (int count = TotUniqNum; count <= gemSize; ++count)
    {
        // 매 count가 바뀔 때마다 
        // 1) map 정보 초기화
        auto iter = mapInclude.begin();
        auto iterEnd = mapInclude.end();
        
        for (; iter != iterEnd; ++iter)
            iter->second = 0;
        
        // 2) queue 비워주기
        qWindow = queue<string>();
        
        // 3) uniqNum 정보 초기화
        curUniqN = 0;
        
        // 초기 Window 세팅
        // 현재 Window에 포함된 보석 조사
        // cout << "count : " << count << endl;
        for (int s = 0; s < count; ++s)
        {
            if (mapInclude[gems[s]] == 0)
                curUniqN += 1;
            
            mapInclude[gems[s]] += 1;
            
            qWindow.push(gems[s]);
        };
        
        // 만약 모두 포함되어 있다면 return;
        if (curUniqN == TotUniqNum)             
        {
            answer = vector<int>{1, count};
            return answer;
        }         
        
        // 이후, 같은 크기의 Window 조사하기
        for (int stN = 1; stN < gemSize - count + 1; ++stN)
        {
            if (stN + count - 1 >= gemSize)
                break;
            
            // 기존 것 제거
            const string& outGem = qWindow.front();
            qWindow.pop();

            mapInclude[outGem] -= 1;

            if (mapInclude[outGem] == 0)
                curUniqN -= 1;

            // 새로운 보석 추가
            const string& newGem = gems[stN + count - 1];

            if (mapInclude[newGem] == 0)
                curUniqN += 1;

            mapInclude[newGem] += 1;
            
            qWindow.push(newGem);

            // 만약 모두 포함되어 있다면 return;
            if (curUniqN == TotUniqNum)             
            {
                answer = vector<int>{stN + 1, stN + count};
                return answer;
            }   
        }
    }
    
    return answer;
}

// 2번째 --> 투포인터
