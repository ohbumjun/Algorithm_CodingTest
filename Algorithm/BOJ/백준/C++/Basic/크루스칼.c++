#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std; //

int check[7];	//노드 연결용, 연결노드가 바뀌는지 체크 --

class Edge{
public:
	int node[2];
	int distance;
	Edge(int a, int b, int distance){
		this->node[0] = a;
		this->node[1] = b;
		this->distance = distance;
	}
	// 비교 연산자 오버로딩을 해야
    // 해당 객체들을 기준으로 sort 함수를 돌릴 수 있다. 
	//간선을 오름차순으로 정렬할때 기준을 distance로 정해줍니다. 
	bool operator<(Edge &edge){
		return this->distance < edge.distance;
	}
};

int getParent(int node){
	if(check[node]==node) return node;
	return getParent(check[node]);
}

//두 노드를 작은값을 기준으로 연결합니다. 
void unionParent(int node1, int node2){
	node1 = getParent(node1);
	node2 = getParent(node2);
	if(node1<node2) check[node2] = node1;
	else check[node1] = node2;
}

//싸이클이 존재하면 true, 아니면 false를 반환
bool isCycle(int node1, int node2){
	node1 = getParent(node1);
	node2 = getParent(node2);
	if(node1==node2) return true;
	else return false;
}

int main(){
	//두 노드를 연결할 간선을 정해줍니다. 
	vector<Edge> v;
	v.push_back(Edge(1, 7, 12));
	v.push_back(Edge(1, 4, 23));
	v.push_back(Edge(1, 2, 26));
	v.push_back(Edge(2, 3, 36));
	v.push_back(Edge(2, 4, 21));
	v.push_back(Edge(2, 5, 45));
	v.push_back(Edge(3, 5, 29));
	v.push_back(Edge(3, 6, 37));
	v.push_back(Edge(3, 7, 55));
	v.push_back(Edge(4, 7, 20));
	v.push_back(Edge(5, 6, 30));
	
	//간선을 오름차순으로 정렬합니다. 
	sort(v.begin(), v.end());
	
	//각 노드는 자기자신이 부모로 초기화해줍니다. 
	for(int i=1;i<=7;++i){
		check[i] = i;
	}
	
	int sum = 0;
	for(int i=0;i<v.size();++i){
		//싸이클이 존재하지 않으면 비용을 더합니다. 
		if(!isCycle(v[i].node[0], v[i].node[1])){
			sum+=v[i].distance;
			unionParent(v[i].node[0], v[i].node[1]);
		}
	}
	
	printf("%d\n", sum);
	
	return 0;
}