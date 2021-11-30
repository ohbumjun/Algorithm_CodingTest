#include <iostream>

class Plus
{
public :
    explicit Plus(int a) :localVar{a}{}
    int operator() (int x) const {return localVar + x;}
private :
    int localVar;
};

int main()
{
    // Stack 영역에 각각 Plus 객체 + 각 객체의 local variable이 생성된다 
    Plus plus3{3};
    Plus plus5{5};

    // 인자는 int x 를 받는다
    // localVar + x 가 return ㄱㅂ사 
    auto lamdaPlus3 = [localVar = 3](int x)
    {
        return localVar + x;
    }
}