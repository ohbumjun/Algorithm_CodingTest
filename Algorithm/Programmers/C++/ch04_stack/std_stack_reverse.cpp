#include<iostream>
#include <vector>
#include <stack>

using namespace std;

// 문자열 뒤집기
string reverse(const string& str)
{
    stack<char> stk;
    for (char c : str)
        stk.push(c);

    string res;
    while (!stk.empty())
    {
        res += stk.top();
        stk.pop();
    }
    return res;
}

// 벡터 뒤집기
template<typename T>
void reverse(vector<T>& vec)
{
    stack<T> stk;
    for (const T& a : vec)
        stk.push(a);
    for (int i = 0; i < vec.size(); i++)
    {
        vec[i] = stk.top();
        stk.pop();
    }
}

int main()
{
    string str1 = "HELLO";
    vector<int> vec {10,20,30,40,50};

	cout << str1 << " -> " << reverse(str1) << endl;
    reverse<int>(vec);
    for(const auto &e : vec)
        cout << e << ", ";
    return 0;
}