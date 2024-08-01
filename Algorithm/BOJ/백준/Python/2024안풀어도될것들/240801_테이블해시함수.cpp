// https://school.programmers.co.kr/learn/courses/30/lessons/147354

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int column;

bool compare(const vector<int>& a, const vector<int>& b)
{
    if (a[column] == b[column])
        return a[0] > b[0];         // 내림차순
    
    return a[column] < b[column];   // 오름차순
}

int solution(vector<vector<int>> data, int col, int row_begin, int row_end) {
    
    vector<int> s_is;
    int answer  = 0;
    column      = col - 1;
    s_is.resize(data.size());
    
    std::sort(data.begin(), data.end(), compare);
    
    for (int i = 0; i < data.size(); ++i)
    {
        vector<int>& d = data[i];
        for (const int& n : d) s_is[i] += (n % (i + 1));
        // cout << s_is[i] << endl;
        if (row_begin - 1 <= i && i <= row_end - 1) 
            answer = answer ^ s_is[i];
    }
    
    
    return answer;
}