/*
>> 우선 순위 큐
- 각각의 데이터에 우선순위(priority queue)가 정의되어 있어서
입력 순서에 상관없이, 우선순위가 가장 높은 데이터가 먼저 출력되는 형태의 자료 구조 

>> priority_queue
template<class T,
         class Container = std::vector<T>,
         class Compare   = std::less<T>>
class priority_queue

- 삽입 순서에 상관없이, 우선순위가 가장 높은 원소가 먼저 출력된다.
- 사용자 정의 타입을 저장할 경우, 비교연산.을 지원해야 한다. 
- push() : 원소 추가        == log(n)
- pop()  : 최상위 원소 제거 == log(n)
- top()  : 최상위 원소 참조 == log(1)

*/

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

template<typename T>
void print_queue(T q)
{
    // q는 복사된 형태의 queue가 들어올 것
    // 여기서의 변화는, 원본 queue에 어떤 변화도 주지 않는다. 
    while(!q.empty())
    {
        cout << q.top() << ", ";
        q.pop();
    }
}

class Student
{
public :
    string name;
    int score;
};

class Student2
{
public :
    string name;
    int score;
    bool operator < (const Student& st) const 
    {
        return score < st.score;
    }
};

int main()
{
    vector<int> vec{4,3,2,5,1};

    // 내림 차순 정렬 
    // 큰 값이 우선 순위가 높음 
    priority_queue<int> pq1;
    for(auto n : vec)
        pq1.push(n);
    print_queue(pq1);

    // 오름 차순 정렬 
    // vec의 모든 정수값을 pq2에 넣으면서 정의 
    // 작은 값이 우선순위가 높음 
    priority_queue<int, vector<int>, greater<int>> pq2(vec.begin(), vec.end());
    print_queue(pq2);

    // 아래들은 오류가 난다
    // 왜냐하면, 우선순위 큐의 경우 , 우선순위가 높은 것이 먼저 출력되도록
    // 내부에서 데이터들을 비교해야 하는데
    // Student class 내에 데이터 비교연산이 없어서 오류가 난다 
    priority_queue<Student> students;
    students.push({"Amelia", 80});

    priority_queue<Student2> students2;
    students.push({"Amelia", 80});

    while(!students2.empty())
    {
        auto& s = students2.top(); // 참조. 형태를 반환한다
        cout << s.name << " ( " << s.score << " ) " << endl;
        students2.pop();
    }
    return 0;
}