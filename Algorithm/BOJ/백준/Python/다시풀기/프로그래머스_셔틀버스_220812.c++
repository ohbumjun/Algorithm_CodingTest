// https://school.programmers.co.kr/learn/courses/30/lessons/17678

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vecBusTimes;
vector<int> vecPTimes;
int MaxLimitBusTime = -1;

// < 사전 준비 >
// 크루원들의 도착 시간을 오름차순 정렬

// <문제 풀이>
// 1. 마지막 셔틀에 자리가 남을 경우
// - 해당 마지막 셔틀을 타고 가면 된다.
// - 콘이 줄을 서야 하는 시간은, 가장 마지막 셔틀이 도착하는 시간

// 2. 마지막 셔틀에 자리가 남지 않을 경우
// - 크루원들이 도착하는 시간 어느 중간에 도착해야 한다는 것
// - 콘을 제외하고, 생각할 때, 셔틀 버스 탑승한 마지막 크루원의 시간 - 1


string solution(int N, int T, int M, vector<string> timetable) {
    
   // 크루원들 시간 구하기 
	vector<int> Crew;

	for (int i = 0; i < timetable.size(); ++i)
	{
		string S_Hour = "";
		S_Hour = S_Hour + timetable[i][0];
		S_Hour = S_Hour + timetable[i][1];
		int Hour = stoi(S_Hour);

		string S_Minute = "";
		S_Minute = S_Minute + timetable[i][3];
		S_Minute = S_Minute + timetable[i][4];
		int Minute = stoi(S_Minute);

		int Time = Hour * 60 + Minute;
		Crew.push_back(Time);
	}

	sort(Crew.begin(), Crew.end());

	// 크루원들 태우기
	int Shuttle_Time = 9 * 60;
	int Crew_Idx = 0;
	int Answer_Time = 0;

	for (int n = 0; n < N; ++n, Shuttle_Time = Shuttle_Time + T)
	{
		int Cnt = 0;

		for (int j = Crew_Idx; j < Crew.size(); ++j)
		{
			// 대기 중인 크루가 있다면
			if (Crew[j] <= Shuttle_Time)
			{
				Crew_Idx++;
				Cnt++;

				// 모두 태웠다면
				if (Cnt == M)
					break;
			}
		}

		// 마지막 셔틀이라면
		if (n == N - 1)
		{
			// 모두 태웠다면 
			// 즉, 마지막 자리가 없다면, 
			if (Cnt == M)
			{
				// 마지막으로 탄 크루의 시간 - 1
				Answer_Time = Crew[Crew_Idx - 1] - 1;
			}
			// 모두 태우지 않았다면
			// 마지막 셔틀 도착 시간
			else
			{
				Answer_Time = Shuttle_Time;
			}
		}
	}

	string StrAnswer;
	StrAnswer.reserve(5);

	int Hour = Answer_Time / 60;
	int Min = Answer_Time % 60;

	if (Hour < 10)
		StrAnswer.append("0");

	StrAnswer.append(to_string(Hour));

	StrAnswer.append(":");

	if (Min < 10)
		StrAnswer.append("0");

	StrAnswer.append(to_string(Min));

	return StrAnswer;
	
}