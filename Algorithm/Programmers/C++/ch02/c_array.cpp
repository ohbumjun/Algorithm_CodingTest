#include <iostream>

using namespace std;

int main()
{
    int scores[5] = {4, 5, 6, 7, 8};

    int sz = size(scores);

    int s = 0;
    for (int i = 0 ; i < sz; i++)
    {
        s += scores[i];
    }

    float m = (float)s / sz;
    cout << m << endl;

    return 0;
}