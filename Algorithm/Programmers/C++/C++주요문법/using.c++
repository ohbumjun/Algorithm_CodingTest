// using
// 별칭을 사용 --> C 에서의 typedef 대신 using
typedef unsigned char uchar;
using uchar = unsigned char;

typedef pair<int, string> pis;
using pis = pari<int, string>;

typedef void (*func)(int);
using func = void(*)(int);

// template 과 활용
template<typenmae T>
using matrix1d = vector<T>;

// 사용 예제
matrix1d<float> vec(3);
void my_function(int n){}
func fp = &my_function;