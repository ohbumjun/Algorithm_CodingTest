#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

struct CompStr
{
    bool operator () (const string& str1, const string& str2)
    {
        return str1 + str2 > str2 + str1; // 330 , 303
    }
};

string solution(vector<int> numbers) {
    
    string answer = "";
    
    vector<string> vecStrings;
    vecStrings.reserve(numbers.size());
    
    // 0) 모두 string 으로 변환
    for (const auto& num : numbers)
        vecStrings.push_back(std::to_string(num));
    
    // 1) 크기 기준 내림 차순
    std::sort(vecStrings.begin(), vecStrings.end(), CompStr());
    
    // 2) Answer 에 붙여넣기
    int totStrSize = 0;
    
    for (const auto& numStr : vecStrings)
        totStrSize += numStr.length();
    
    answer.reserve(totStrSize);
    
    for (const auto& numStr : vecStrings)
        answer.append(numStr);
    
    if (answer[0] == '0')
        return "0";
    
    return answer;
}