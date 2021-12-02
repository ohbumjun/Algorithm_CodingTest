#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class MaxHeap
{
private :
    vector<int> vec;
public :
    MaxHeap() : vec(1){}
    void push(int value)
    {
        vec.push_back(value);
        heapify_up(vec.size() - 1);
    };
    void pop()
    {
        // 루트 노드에, 가장 마자믹 노드를 넣는다
        // Heap의 경우, 배열 맨 앞 idx 은 비워두고 사용한다. 
        vec[1] = vec.back();
        vec.pop_back();
        heapify_down(1);
    }
    void heapify_up(int i)
    {
        // i 위치에 새로운 원소 삽입, i는 1보다 큼(루트 노드가 아님)
        if (i > 1 && vec[i] > vec[parent(i)])
        {
            swap(vec[i], vec[parent(i)]);
            heapify_up(parent(i));
        }
    }
    void heapify_down(int i)
    {
        int largest = i;
        if (left(i) < vec.size() && vec[left(i)] > vec[largest])
            largest = left(i);
        if (right(i) < vec.size() && vec[right(i)] > vec[largest])
            largest = right(i);
        if (largest != i)
        {
            swap(vec[i], vec[largest]);
            heapify_down(largest);
        }
    }
    int top() const 
    {
        return vec[1];
    }
    void clear()
    {
        vec.clear();
        vec.push_back(0);
    }
    int size()  
    {
        return vec.size() == 1;
    }
    bool empty()
    {
        return vec.size() == 1;
    }
    void print()
    {
        for(const auto& n : vec)
            cout << n << endl;
        cout << endl;
    }
private :
    int parent(int i)
    {
        return i / 2;
    }
    int left(int i)
    {
        return 2 * i;
    }
    int right(int i)
    {
        return 2 * i + 1;
    }
    
};

int main()
{
    MaxHeap heap;
    heap.push(1);
    heap.push(5);
    heap.push(7);
    heap.push(8);
    heap.push(3);
    heap.push(9);
    heap.push(10);
    heap.print();

    while(!heap.empty())
    {
        cout << heap.top() << ", ";
        heap.pop();
    }
    cout << endl;
}