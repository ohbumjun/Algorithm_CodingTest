// https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

/*
1) DFS + Memoization 

https://www.youtube.com/watch?v=JLoWc3v0SiE

각 job 에 대해 2가지 선택이 있다.
해당 job 을 선택할지 말지

st time 기준 정렬한다.
만약 해당 job 을 선택하면, 이후에 나오는 job 중에서
앞서 선택한 job 과 겹치는 job 은 선택하지 않는다.

만약 해당 job 을 선택하지 않는다면, 그 다음 st time job 으로
넘어가면 된다.

=> 시간 초과가 발생한다.
왜냐하면 nxtIdx 를 구할 때, o(n) 의 시간이 걸리면서, 뒤에 있는 모든
job 을 확인하는 과정을 거치기 때문이다.
*/
class Solution {
public:
    struct Job
    {
        int st; 
        int ed;
        int profit;

        bool operator < (const Job& other)
        {
            return st < other.st;
        }
    };
    vector<Job> jobs;
    vector<int> memoization;

    // 해당 idx job 이후의 최대 retVal 
    int dfs(int idx)
    {
        if (idx == jobs.size()) return 0;

        if (memoization[idx]) return memoization[idx];

        int retVal = 0;

        // Job include X -> 바로 다음 idx + 1 로 넘어간다.
        retVal = dfs(idx + 1);

        // Job Include  -> 그 다음 가능한 job 의 idx : 'j' 을 선택한 경우
        int nxtIdx = idx + 1;

        while(nxtIdx < jobs.size())
        {
            if (jobs[nxtIdx].st >= jobs[idx].ed) break;
            nxtIdx += 1;
        }

        // dfs(nxtIdx) : nxtIdx 에 해당하는 job 을 선택할 수도 있고 선택 안할 수도 있다.
        retVal = max(retVal, jobs[idx].profit + dfs(nxtIdx));

        memoization[idx] = retVal;

        return retVal;
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<int> dp;
        jobs.reserve(startTime.size());
        memoization.resize(startTime.size());

        for (int i = 0; i < startTime.size(); ++i)
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        
        sort(jobs.begin(), jobs.end());

        return dfs(0);
    }
};

/*
2) 그렇다면, nxtIdx 를 찾는 방식을 이진 탐색으로 변경하면 된다.
*/

class Solution {
public:
    struct Job
    {
        int st; 
        int ed;
        int profit;

        bool operator < (const Job& other)
        {
            return st < other.st;
        }
    };
    vector<Job> jobs;
    vector<int> memoization;

    // 해당 idx job 이후의 최대 retVal 
    int dfs(int idx)
    {
        if (idx == jobs.size()) return 0;

        if (memoization[idx]) return memoization[idx];

        int retVal = 0;

        // Job include X -> 바로 다음 idx + 1 로 넘어간다.
        retVal = dfs(idx + 1);

        // Job Include  -> 그 다음 가능한 job 의 idx : 'j' 을 선택한 경우
        int nxtIdx = idx + 1;

        // while(nxtIdx < jobs.size())
        // {
        //     if (jobs[nxtIdx].st >= jobs[idx].ed) break;
        //     nxtIdx += 1;
        // }

        int st = idx + 1, ed = jobs.size();
        while(st <= ed)
        {
            int mid = (st + ed) / 2;

            if (mid == jobs.size()) 
            {
                nxtIdx = mid;
                break;
            }

            if (jobs[mid].st >= jobs[idx].ed)
            {
                nxtIdx = mid;
                ed = mid - 1;
            }
            else
            {
                st = mid + 1;
            }
        }

        // cout << "idx, nxtIdx : " << idx << "," << nxtIdx << endl;

        // dfs(nxtIdx) : nxtIdx 에 해당하는 job 을 선택할 수도 있고 선택 안할 수도 있다.
        retVal = max(retVal, jobs[idx].profit + dfs(nxtIdx));

        memoization[idx] = retVal;

        // cout << "retVal : " << retVal << endl;

        return retVal;
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<int> dp;
        jobs.reserve(startTime.size());
        memoization.resize(startTime.size());

        for (int i = 0; i < startTime.size(); ++i)
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        
        sort(jobs.begin(), jobs.end());

        return dfs(0);
    }

    // 1  ~ 2   > 5
    // 1  ~  3  > 6
    // 1  ~   4 > 4
};