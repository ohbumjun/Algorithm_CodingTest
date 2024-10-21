// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/description/

class Solution {
public:
    int minOperations(vector<int>& target, vector<int>& arr) {
        vector<int> indices;
        unordered_map<int, int> numToIndex;

        // 자. arr 요소를 각각 target 에서 찾을 것이다.
        // 이를 쉽게 하기 위해서, target 각 요소가 몇번째 idx 에 있는지 map 에 저장한다.
        for (int i = 0; i < target.size(); ++i)
            numToIndex[target[i]] = i;

        // target 에서 찾은 arr 의 원소들만 indices 에 "몇번째 idx" 인지 그 정보를 넣어준다.
        for (const int a : arr)
            if (const auto it = numToIndex.find(a); it != numToIndex.end())
                indices.push_back(it->second);

        return target.size() - lengthOfLIS(indices);
    }

    private:
    // Same as 300. Longest Increasing Subsequence
    int lengthOfLIS(vector<int>& nums) {
        // tail[i] := the minimum tail of all the increasing subsequences having
        // length i + 1
        vector<int> tail;

        // tail 맨 마지막 원소에는, 가장 큰 값이 들어가 있게 된다.
        for (const int num : nums)
        {
            // cout << "---" << endl;
            // cout << "num : " << num << endl;
            // cout << "bef tail" << endl;
            // for (int t : tail) cout << t << ".";
            // cout << endl;

            if (tail.empty() || num > tail.back())  // tail 이 비거나, 현재 것이 가장 크면 push
                tail.push_back(num);
            else
            {
                // 즉, 자기보다 크거나 같은 요소에, 자기 자신을 넣어버리는 것.
                // 해당 값은, 맨 마지막 tail.back 이 될 수도 있다.
                // ex) tail 에 0,5 가 있었고, num 이 4 라면, 0,4 로 tail 이 변경된다.
                // 사실 이 lower_bound 함수를 이분 탐색으로 변경하면 될 것 같다.
                int foundIdx = firstGreaterEqual(tail, num);
                // cout << "foundIdx : " <<foundIdx << endl;
                tail[foundIdx] = num;
            }
            // cout << "aft tail" << endl;
            // for (int t : tail) cout << t << ".";
            // cout << endl;
        }

        return tail.size();
    }

    private:
    int firstGreaterEqual(const vector<int>& A, int target) {
        // LCS 에서 num 보다 크거나 같은 가장 작은 element return
        // 이를 통해서, LIS 가 increasing order 을 유지하면서
        // 새로운 element 를 LIS 에 넣어줄 수 있다.
        return ranges::lower_bound(A, target) - A.begin();
    }
};