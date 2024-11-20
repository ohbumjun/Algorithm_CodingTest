// https://leetcode.com/problems/ipo/
// https://www.youtube.com/watch?v=1IUzNJ6TPEM&t=309s

class Solution {
public:
    struct ProfitStruct
    {
        int profit; // max heap
        int index;

        bool operator < (const ProfitStruct& project) const
        {
            return profit < project.profit;
        }
    };

    struct CapitalStruct
    {
        int capital;    // min heap
        int index;

        bool operator < (const CapitalStruct& project) const
        {
            return capital > project.capital;
        }
    };

    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) 
    {
        priority_queue<CapitalStruct>   minCapitalHeap;
        priority_queue<ProfitStruct>    maxProfitHeap;
        int cnt = 0;

        for (int idx = 0; idx < profits.size(); ++idx)
            minCapitalHeap.push(CapitalStruct(capital[idx], idx));

        while(cnt < k)
        {
            while(!minCapitalHeap.empty() && minCapitalHeap.top().capital <= w)
            {
                int idx = minCapitalHeap.top().index;
                maxProfitHeap.push(ProfitStruct(profits[idx], idx));
                minCapitalHeap.pop();
            }

            if (maxProfitHeap.empty()) break;

            w += maxProfitHeap.top().profit;
            maxProfitHeap.pop();
            cnt += 1;
        }

        // profit 기반 max heap
        // -> 
        // capital 기반 min heap
        // -> 

        // 일단 min heap 으로 모든 녀석이 들어가 있다.
        // 일단 현재 w 보다 min heap 에서 꺼낸 애가 capital 이 작거나 같으면
        // profit 기반 max heap 에 push 한다.
        // 자. 그러다가, capital 이 더 w 보다 크면. 이제 그만 pop

        // 자. 이제 profit 기반 max heap 에서 최고 profit 을 꺼낸다.
        // 그리고 w 를 update
        // 이제 또 다시 min heap 에서 pop

        return w;
    }
};