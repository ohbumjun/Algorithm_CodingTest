#include <iostream>

template<typename T1, typename T2>
void Print(T1 t1, T2 t2){};

template<typename T1>
void Print(T1 t1, int){}