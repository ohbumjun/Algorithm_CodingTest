#include <string>
#include <vector>
#include <algorithm>

#define END 11

using namespace std;

vector<int> vecAnswer;
int MaxScore = 0;

void DFS(int N, int ArrowLeft, int PrevIndex,
    vector<int>& vecApichScore, vector<int>& vecRyanScore) //
{
    // 더이상 쏠 화살이 없다면
    if (ArrowLeft == 0)
    {
        // 여기서 점수를 비교해야 한다.

        int RyanScr = 0;
        int ApichScr = 0; //

        // cout << "Hello" << endl;

        // 맨 마지막 0점은 비교하지 않는다.
        for (int i = 0; i < 10; i++)
        {
            int Score = 10 - i;

            if (vecRyanScore[i] == 0 && vecApichScore[i] == 0)
                continue;

            if (vecRyanScore[i] > vecApichScore[i])
            {
                RyanScr += Score;
            }
            else if (vecRyanScore[i] <= vecApichScore[i])
            {
                ApichScr += Score;
            }
        }

        // Apich Score가 더 크거나 같다면 X 
        if (ApichScr >= RyanScr)
            return;

        // 비교
        /*
        cout << "vec RyanScore" << RyanScr << endl;
        for (const auto& elem : vecRyanScore)
            cout << elem << " ";
        cout << endl;

        cout << "vec ApichScore" << ApichScr << endl;
        for (const auto& elem : vecApichScore)
            cout << elem << " ";
        cout << endl;
        cout << endl;
        */

        int DiffScore = RyanScr - ApichScr; //

        // 현재 최대값과 비교한다
        if (MaxScore < DiffScore)
        {
            MaxScore = DiffScore;
            vecAnswer = vecRyanScore;
        }
        else if (MaxScore == DiffScore)
        {
            for (int i = END - 1; i >= 0; i--)
            {
                if (vecAnswer[i] < vecRyanScore[i])
                {
                    vecAnswer = vecRyanScore;
                    break;
                }
                else if (vecAnswer[i] > vecRyanScore[i])
                    break;
            }
        }

        return;
    }
    // 그게 아니라면, 중복 조합을 만들어나간다.
    for (int i = PrevIndex; i < END; i++)
    {
        vecRyanScore[i] += 1;
        DFS(N, ArrowLeft - 1, i, vecApichScore, vecRyanScore);
        vecRyanScore[i] -= 1;
    }
}

vector<int> solution(int n, vector<int> info) {

    vector<int> vecRyanScore;
    vecRyanScore.resize(END); // 11 발을 쏠 것이다.

    // 라이언이 쏠 수 있는 모든 경우의 수를 구하고 --> 중복 조합
    // 각각에 대해 점수차를 계산해서
    DFS( END, n, 0, info, vecRyanScore);

    // 나중에 정렬 이후, 정답 출력 
    // sort(vecAnswer.begin(), vecAnswer.end());

    // vecAnswer 가 비어있다면 우승할 수 없는 경우
    if (vecAnswer.empty())
    {
        std::vector<int> Answer;
        Answer.push_back(-1);
        return Answer;
    }
    else
    {
        return vecAnswer;
    }
}