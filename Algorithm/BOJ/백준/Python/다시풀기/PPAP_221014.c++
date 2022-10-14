// https://www.acmicpc.net/problem/16120

#include <bits/stdc++.h>

using namespace std;

int main(void) {
	string str, ppap;
	cin >> str;

	for (auto& i : str) {
		ppap.push_back(i);

		if (ppap.size() < 4)
			continue;

		while (ppap.size() >= 4 && ppap.substr(ppap.size() - 4, 4) == "PPAP") {
			for (int j = 0; j < 4; j++)
				ppap.pop_back();
			ppap.push_back('P');
		}
	}

	cout << (ppap == "P" ? "PPAP" : "NP") << '\n'; //
	return 0;
}