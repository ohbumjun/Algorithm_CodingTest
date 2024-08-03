#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

struct NumStr
{
    NumStr(int n)
    {
        nStr = to_string(n);
        num = n;
    }
    
    bool operator < (const NumStr& other)
    {
        int shortSize   = other.nStr.size() < nStr.size() ? other.nStr.size() : nStr.size();
        int longSize    = other.nStr.size() > nStr.size() ? other.nStr.size() : nStr.size();
        int compSize    = other.nStr.size() < nStr.size() ? other.nStr.size() : nStr.size();
        bool selfSmall  = other.nStr.size() < nStr.size() ? false : true;
        
    }
    
    string nStr;
    int num;
};

string solution(vector<int> numbers) 
{
    // 가장 첫번째 숫자를 기준으로 내림차순
    // 이후 만나는 모든 문자를 add 한다.
    string answer;
    vector<NumStr> numStrs;
    numStrs.reserve(numbers.size());
    for (int n : numbers)
    {
        numStrs.push_back(NumStr(n));
    }
    std::sort(numStrs.begin(), numStrs.end());
    for (const NumStr& nStr : numStrs)
    {
        answer += nStr.nStr;
    }
    return answer;
}