# https://www.acmicpc.net/problem/12886


'''
< 해설 >

정점 : 돌에 있는 돌의 개수 
( A, B, C )

간선 : ( A, B, C ) ->  ( A``, B``, C`` )


정점의 개수 : ( 최대값 500 ) ^ 3 ??
아니다.

한 집단에, 최대 정점이 몇개까지 올 수 있는지를
생각해야 한다

500 499 500
500 998 1
1000 498 1

즉, 한집단에 올 수 있는 정점의 최대개수는
1000 개가 되는 것이다 

따라서 , 정점의 최대개수는 1000 ^ 3

너무 크다. 10억이라는 크기

자세히 생각해보면,
3개 집단에 있는, 전체 돌의 개수는 변하지 않는다 
500 499 500
500 998 1
1000 498 1

위의 변화 과정에서도, 유일하게
변하지 않는 것은
" 전체 돌의 개수 " 인 것이다

전체 돌의 개수 : S 
첫번째 집단 돌의 개수 : A
두번째 집단 돌의 개수 : B
세번째 집단 돌의 개수 : S - A - B

즉, 우리가 고려해야 하는 범위는
A, B 만 있으면 되는 것이다

즉, ( 1500 ) ^ 2 가 되는 것이다 

--------------------------------------

문제에서 요구하는 것은
3개 집단 돌의 개수가 모두 
같아질 수 있는지를 보는 것이다

즉, ( A, B, C ) => ( S/3, S/3, S/3 )
이 될 수 있는지를 보는 것이다 

다른 말로 하면
( A, B, C ) => ( S/3, S/3, S/3 )
왼쪽에서,
오른쪽으로
이동할 수 있는지를 보는 문제이다 

--------------------------------------
< 최소 거리, 최소 횟수> 를 물어보는 문제가 아니다

따라서, BFS, DFS 둘다 사용가능하다 

'''

sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
1) 주어진 3개의 원소를 
x, y, z 라고 한다면
x, y 로만 생각해도 된다
전체 주어진 돌의 개수를 sum이라 하면, sum은 변하지 않기 때문에
나머지 z는 sum - x - y로도 정의할 수 있다
 
'''
check = [[0] * 1501 for _ in range(1501)]
x, y, z = map(int, input().split())
sum = x + y + z


def go(x, y):
    global sum
    # 이미 그곳을 방문했으면, 다시 수행할 필요 없다 ( 해당 돌의 경우수를 만들어본 적이 있으면 또해볼 필요가 없다 )
    if check[x][y]:
        return
    check[x][y] = 1
    a = [x, y, sum-x-y]
    # 이제 해당 배열에 대해서, 모든 경우에 대해 이동시킨다
    for i in range(3):
        for j in range(3):
            # 아래의 조건을 넣어주는 이유는
            # 1) arr[i], arr[j]는 같아서는 안된다는 것
            # 2) arr[i] > arr[j] 일 경우, 이것이 나중에 arr[j]가 되고 arr[i] 가 될 때, 반복될 수 있다
            if a[i] < a[j]:
                b = [x, y, sum - x - y]
                b[i] += a[i]
                b[j] -= a[i]
                # 왜 b[0], b[1]이 들어가는 것일까?
                # 어차피 2개 검사하는 것이므로, 2개 원소 넣는 것은 알겠다
                # b[i], b[j]를 넣어줘야 하는 것이 아닌가 ?
                # 아니지, 우리는, 앞에 2개 원소만을 기준으로 계속 갖고 노는 것이다 !!
                go(b[0], b[1])


# 반드시 필요한 코드
# 애초부터 3개가 모두 동일할 수 없는 경우도 있기 때문이다
if sum % 3 != 0:
    print(0)
else:
    go(x, y)
    if check[sum//3][sum//3]:
        print(1)
    else:
        print(0)


'''
C++

#include <iostream>
#include <queue>
using namespace std;
bool check[1501][1501];
int sum;
void go(int x, int y) {
    if (check[x][y]) return;
    check[x][y] = true;
    int a[3] = {x, y, sum-x-y};
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (a[i] < a[j]) {
                int b[3] = {x, y, sum-x-y};
                b[i] += a[i];
                b[j] -= a[i];
                go(b[0], b[1]);
            }
        }
    }
}
int main() {
    int x, y, z;
    cin >> x >> y >> z;
    sum = x + y + z;
    if (sum % 3 != 0) {
        cout << 0 << '\n';
        return 0;
    }
    go(x, y);
    if (check[sum/3][sum/3]) {
        cout << 1 << '\n';
    } else {
        cout << 0 << '\n';
    }
    return 0;
}


'''
