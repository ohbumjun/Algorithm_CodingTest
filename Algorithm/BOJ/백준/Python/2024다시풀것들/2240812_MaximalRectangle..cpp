// https://leetcode.com/problems/maximal-rectangle/

class Solution {
public:
    int largestRectangle(const vector<int>& heights) {
        int maxArea = 0;

        stack<int> sLastHeights;
        stack<int> sLastIdxs;

        sLastHeights.push(heights[0]);
        sLastIdxs.push(0);

        for (int idx = 1; idx < heights.size(); ++idx) {
            int curH = heights[idx];
            int stIdx = idx;
            if (sLastHeights.top() <= curH) {
                sLastHeights.push(curH);
                sLastIdxs.push(idx);
                continue;
            }

            while (!sLastHeights.empty() && sLastHeights.top() > curH) {
                int topH = sLastHeights.top();
                int topIdx = sLastIdxs.top();

                sLastHeights.pop();
                sLastIdxs.pop();

                int area = topH * (idx - topIdx);
                maxArea = max(area, maxArea);
                stIdx = topIdx;
            }

            sLastHeights.push(curH);
            sLastIdxs.push(stIdx);
        }

        while (!sLastHeights.empty()) {
            int topH = sLastHeights.top();
            int topIdx = sLastIdxs.top();

            sLastHeights.pop();
            sLastIdxs.pop();

            int area = topH * (heights.size() - topIdx);
            maxArea = max(area, maxArea);
        }

        return maxArea;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        // 각 row 별로 histogram 정보를 만든다.
        // 각 row 를 돌면서, 최대 rectangle 을 구해간다.
        // 그렇게 마지막 row 까지 진행한다.
        int maxArea = 0;
        vector<vector<int>> heightsMatrix;
        heightsMatrix.resize(matrix.size());
        for (vector<int>& hMat : heightsMatrix)
            hMat.resize(matrix[0].size());

        for (int r = 0; r < matrix.size(); ++r) {
            const vector<char>& matrixRow = matrix[r];
            for (int c = 0; c < matrixRow.size(); ++c) {
                if (matrixRow[c] == '0')
                    continue;
                if (r - 1 >= 0)
                    heightsMatrix[r][c] = heightsMatrix[r - 1][c] + 1;
                else
                    heightsMatrix[r][c] = 1;
            }
        }

        for (int r = 0; r < heightsMatrix.size(); ++r) {
            int area = largestRectangle(heightsMatrix[r]);
            maxArea = maxArea < area ? area : maxArea;
        }

        return maxArea;
    }
};