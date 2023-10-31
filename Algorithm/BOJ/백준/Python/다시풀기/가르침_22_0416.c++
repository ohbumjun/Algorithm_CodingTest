#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>
#include <string>
#include <cmath>
#include <climits>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

#define NUM_MAX 50 + 1

int N, K;
vector<string> vecWords;
vector<int> vecWordsInt;
int ANS = -1;

void input()
{
    cin >> N >> K;

    vecWords.reserve(N);

    std::string strIn;

    for (int i = 0; i < N; ++i)
    {
        std::cin >> strIn;
        vecWords.push_back(strIn);

        int WordInt = 0;

        for (size_t i = 0; i < strIn.length(); i++)
        {
            WordInt |= (1 << (strIn[i] - 'a'));
        }
        vecWordsInt.push_back(WordInt);
    }
}


void LearnWord(int NumWords, int PrevLearnedIdx, int CurrentWord)
{
    if (NumWords == K - 5)
    {
        int CanLearnNum = 0;

        // 모든 알파벳들을 돌면서
        size_t WordSize = vecWordsInt.size();

        // cout << "CurrentWord    : " << bitset<32>(CurrentWord) << endl;
    	// printf("CurrentWord : %d\n", CurrentWord);

        for (size_t i = 0; i < WordSize; ++i)
        {
            // cout << "vecWordsInt[i] : " << bitset<32>(vecWordsInt[i]) << endl;
            // cout << "learned Word : " << bitset<32>(vecWordsInt[i] & CurrentWord) << endl;

            if ((vecWordsInt[i] & CurrentWord) == vecWordsInt[i])
            {
                CanLearnNum += 1;
            }
        }

    	// cout << endl;

        if (ANS < CanLearnNum)
            ANS = CanLearnNum;

        return;
    }

    for (int i = PrevLearnedIdx + 1; i < 26; i++)
    {
        if (CurrentWord & (1 << i) == i)
            continue;
        int NewWord = CurrentWord | ((1 << i));
        LearnWord(NumWords + 1, i, NewWord);
    }
}

void Calculate()
{
    // 먼저, antic 라는 5개의 글자는 무조건 가르쳐야 한다.
	// 만약 5글자보다 K가 작다면 0을 출력한다.
    if (K < 5)
    {
        ANS = 0;
        return;
    }

    int LearnedWord = 0;

    LearnedWord |= 1 << ('a' - 'a');
    LearnedWord |= 1 << ('c' - 'a');
    LearnedWord |= 1 << ('n' - 'a');
    LearnedWord |= 1 << ('t' - 'a');
    LearnedWord |= 1 << ('i' - 'a');

	// 26개의 알파벳 중에서 K 를 뽑는 모든 경우의 수 조사
    // 하지만, 결과적으로 21개 중에서 K - 5 개의 알파벳들을 뽑는 경우들을 조사해야 한다.

    // 각 경우에 대해서, 모든 알파벳들을 돌면서, 읽을 수 있는 수인지 아닌지 조사하기

    // 단, string 판별시, bit 단위로 비교하는 로직을 적용한다.
    LearnWord(0, -1, LearnedWord);
}


int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input_c.txt", "r", stdin);

    input();

    Calculate();

    std::cout << ANS;

    return 0;
}