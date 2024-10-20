// https://school.programmers.co.kr/learn/courses/30/lessons/42746

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(const string& a, const string& b)
{
    return a + b > b + a;
}

string solution(vector<int> numbers) 
{
    // 가장 첫번째 숫자를 기준으로 내림차순
    // 이후 만나는 모든 문자를 add 한다.
    string answer;
    vector<string> numStrs;
    numStrs.reserve(numbers.size());
    
    for (int n : numbers) numStrs.push_back(to_string(n));
    
    std::sort(numStrs.begin(), numStrs.end(), compare);
    
    for (const string& nStr : numStrs)
        answer += nStr;
    
    if (answer[0] == '0') answer = '0';
    
    return answer;
}