# https://www.acmicpc.net/problem/16939

'''
구현해야할 사항은 2가지이다
1) 큐브를 한번 정확하게 돌리기 
2) 큐브를 풀었는지 아닌지 검사하기 --> 모든 면이 같은지 확인

사실 여기서 제일 까다로운 것은
한번 돌리는 과정이다.

Notion 참고

'''


def check(a):
    for i in range(6):
        for j in range(4):
            if a[i*4+1] != a[i*4+j+1]:
                return False
    return True


def lu(b):
    a = b[:]
    temp = a[1]
    a[1] = a[5]
    a[5] = a[9]
    a[9] = a[24]
    a[24] = temp
    temp = a[3]
    a[3] = a[7]
    a[7] = a[11]
    a[11] = a[22]
    a[22] = temp
    return a


def ld(b):
    a = lu(b)
    a = lu(a)
    a = lu(a)
    return a


def ru(b):
    a = b[:]
    temp = a[2]
    a[2] = a[6]
    a[6] = a[10]
    a[10] = a[23]
    a[23] = temp
    temp = a[4]
    a[4] = a[8]
    a[8] = a[12]
    a[12] = a[21]
    a[21] = temp
    return a


def rd(b):
    a = ru(b)
    a = ru(a)
    a = ru(a)
    return a


def ul(b):
    a = b[:]
    temp = a[13]
    a[13] = a[5]
    a[5] = a[17]
    a[17] = a[21]
    a[21] = temp
    temp = a[14]
    a[14] = a[6]
    a[6] = a[18]
    a[18] = a[22]
    a[22] = temp
    return a


def ur(b):
    a = ul(b)
    a = ul(a)
    a = ul(a)
    return a


def dl(b):
    a = b[:]
    temp = a[15]
    a[15] = a[7]
    a[7] = a[19]
    a[19] = a[23]
    a[23] = temp
    temp = a[16]
    a[16] = a[8]
    a[8] = a[20]
    a[20] = a[24]
    a[24] = temp
    return a


def dr(b):
    a = dl(b)
    a = dl(a)
    a = dl(a)
    return a


def fl(b):
    a = b[:]
    temp = a[3]
    a[3] = a[17]
    a[17] = a[10]
    a[10] = a[16]
    a[16] = temp
    temp = a[4]
    a[4] = a[19]
    a[19] = a[9]
    a[9] = a[14]
    a[14] = temp
    return a


def fr(b):
    a = fl(b)
    a = fl(a)
    a = fl(a)
    return a


def bl(b):
    a = b[:]
    temp = a[1]
    a[1] = a[18]
    a[18] = a[12]
    a[12] = a[15]
    a[15] = temp
    temp = a[2]
    a[2] = a[20]
    a[20] = a[11]
    a[11] = a[13]
    a[13] = temp
    return a


def br(b):
    a = bl(a)
    a = bl(a)
    a = bl(a)
    return a


a = [0] + list(map(int, input().split()))
if check(lu(a)) or check(ld(a)) or check(ru(a)) or check(rd(a)):
    print(1)
elif check(ul(a)) or check(ur(a)) or check(dl(a)) or check(dr(a)):
    print(1)
elif check(fl(a)) or check(fr(a)) or check(bl(a)) or check(br(a)):
    print(1)
else:
    print(0)

'''
C++

#include <iostream>
#include <vector>
using namespace std;
int n = 24;
bool check(vector<int> a) {
    for (int i=0; i<6; i++) {
        for (int j=0; j<4; j++) {
            if (a[i*4+1] != a[i*4+j+1]) return false;
        }
    }
    return true;
}
vector<int> lu(vector<int> a) {
    int temp = a[1];
    a[1] = a[5];
    a[5] = a[9];
    a[9] = a[24];
    a[24] = temp;
    temp = a[3];
    a[3] = a[7];
    a[7] = a[11];
    a[11] = a[22];
    a[22] = temp;
    return a;
}
vector<int> ld(vector<int> a) {
    a = lu(a);
    a = lu(a);
    a = lu(a);
    return a;
}
vector<int> ru(vector<int> a) {
    int temp = a[2];
    a[2] = a[6];
    a[6] = a[10];
    a[10] = a[23];
    a[23] = temp; 
    temp = a[4];
    a[4] = a[8];
    a[8] = a[12];
    a[12] = a[21];
    a[21] = temp;
    return a;
}
vector<int> rd(vector<int> a) {
    a = ru(a);
    a = ru(a);
    a = ru(a);
    return a;
}
vector<int> ul(vector<int> a) {
    int temp = a[13];
    a[13] = a[5];
    a[5] = a[17];
    a[17] = a[21];
    a[21] = temp;
    temp = a[14];
    a[14] = a[6];
    a[6] = a[18];
    a[18] = a[22];
    a[22] = temp;
    return a;
}
vector<int> ur(vector<int> a) {
    a = ul(a);
    a = ul(a);
    a = ul(a);
    return a;
}
vector<int> dl(vector<int> a) {
    int temp = a[15];
    a[15] = a[7];
    a[7] = a[19];
    a[19] = a[23];
    a[23] = temp;
    temp = a[16];
    a[16] = a[8];
    a[8] = a[20];
    a[20] = a[24];
    a[24] = temp;
    return a;
}
vector<int> dr(vector<int> a) {
    a = dl(a);
    a = dl(a);
    a = dl(a);
    return a;
}
vector<int> fl(vector<int> a) {
    int temp = a[3];
    a[3] = a[17];
    a[17] = a[10];
    a[10] = a[16];
    a[16] = temp;
    temp = a[4];
    a[4] = a[19];
    a[19] = a[9];
    a[9] = a[14];
    a[14] = temp;
    return a;
}
vector<int> fr(vector<int> a) {
    a = fl(a);
    a = fl(a);
    a = fl(a);
    return a;
}
vector<int> bl(vector<int> a) {
    int temp = a[1];
    a[1] = a[18];
    a[18] = a[12];
    a[12] = a[15];
    a[15] = temp;
    temp = a[2];
    a[2] = a[20];
    a[20] = a[11];
    a[11] = a[13];
    a[13] = temp;
    return a;
}
vector<int> br(vector<int> a) {
    a = bl(a);
    a = bl(a);
    a = bl(a);
    return a;
}
int main() {
    vector<int> a(n+1);
    for (int i=1; i<=n; i++) {
        cin >> a[i];
    }
    if (check(lu(a)) || check(ld(a)) || check(ru(a)) || check(rd(a))) {
        cout << 1 << '\n';
        return 0;
    }
    if (check(ul(a)) || check(ur(a)) || check(dl(a)) || check(dr(a))) {
        cout << 1 << '\n';
        return 0;
    }
    if (check(fl(a)) || check(fr(a)) || check(bl(a)) || check(br(a))) {
        cout << 1 << '\n';
        return 0;
    }
    cout << 0 << '\n';
    return 0;
}


'''
