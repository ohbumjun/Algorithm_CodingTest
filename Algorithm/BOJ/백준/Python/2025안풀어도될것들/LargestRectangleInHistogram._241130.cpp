// https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // 일단 현재 height 랑 answer 비교
        // stack top 보다 크거나 같으면 계속 추가
        // 낮으면, stack 에서 계속 pop 하기
        // 자기보다 작거나 같은 숫자가 나올 때까지 pop
        // 다시 add 할 때는 st idx 를 마지막 pop idx 로
        // 마지막 stack 을 비우면서 해당 st idx ~ 마지막 idx 를
        // width 로 하고, height 를 더하여 area 를 구한다.
        int maxArea = 0;
        std::stack<int> slastHeight;
        std::stack<int> slastIdx;

        slastHeight.push(heights[0]);
        slastIdx.push(0);

        for (int idx = 1; idx < heights.size(); ++idx) {
            int curH = heights[idx];
            int stIdx = idx;

            if (slastHeight.top() <= curH) {
                slastHeight.push(curH);
                slastIdx.push(idx);
                continue;
            }

            while (slastHeight.empty() == false && slastHeight.top() > curH) {
                int topH = slastHeight.top();
                int topIdx = slastIdx.top();

                slastHeight.pop();
                slastIdx.pop();

                int area = topH * (idx - topIdx);
                maxArea = maxArea < area ? area : maxArea;
                stIdx = topIdx;
            }
            slastHeight.push(curH);
            slastIdx.push(stIdx);
        }

        while (slastHeight.empty() == false) {
            int topH = slastHeight.top();
            int topIdx = slastIdx.top();

            slastHeight.pop();
            slastIdx.pop();

            int area = topH * (heights.size() - topIdx); //
            maxArea = maxArea < area ? area : maxArea;
        }

        return maxArea;
    }
};