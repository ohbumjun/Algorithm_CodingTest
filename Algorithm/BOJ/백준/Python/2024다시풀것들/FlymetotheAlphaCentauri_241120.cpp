// https://noname-yet.tistory.com/15
// https://www.acmicpc.net/problem/1011

#include <iostream>
using namespace std;

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int T;
	int x, y;
	cin >> T;
	long long* arr = new long long[100000];
	arr[0] = 0;
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;
	for (int i = 4; i < 100000; i++)
	{
		if (i % 2 == 0)
		{
			arr[i] = arr[i - 2] + (i / 2) * 2;
		}
		else
		{
			arr[i] = arr[i - 2] + 2 * (i / 2) + 1;
		}
	}
	for (int i = 0; i < T; i++)
	{
		cin >> x >> y;
		int num = 0;
		while (true)
		{
			if (y - x <= arr[num])
			{
				cout << num << "\n";
				break;
			}
			else
			{
				num++;
			}
		}
	}
	
	return 0;
}