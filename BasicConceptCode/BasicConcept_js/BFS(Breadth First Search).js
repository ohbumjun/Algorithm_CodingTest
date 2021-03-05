// 자신의 주소 + 자식노드들의 주소를 담은 Node
class Node {
    constructor(data){
        this.data = data// 다른 노드와 차별점을 두는 데이터
        this.children = [ ] // 자식들과의 정보(주소)를 담는 배열
    }

    add(data){
        // 자식 추가하는 메소드
        this.children.push(new Node(data)) // 자식 노드 생성 후, 바로 배열에 저장
    }

    remove(data){
        // 자식 정보 지우는 메소드
        this.children = this.children.filter(child => child.data === data ? false : true)
    }
}




class Tree{
    constructor (){
        this.root = null;
    }

    BFS(fn){
        // 인자로 callback 함수를 받는다

        const unvisitedQueue = [this.root]
        while( unvisitedQueue.length != 0){
            const current = unvisitedQueue.shift() // dequeue
            unvisitedQueue.push(...current.children) // 현재 부모 노드의 자식들을 모두 넣는다
            fn(current)
            // 현재 노드를 가지고 callback 함수 실행
            // dequeue한 노드를 목표한 배열에 추가하기 
        }
    }
}

const lettersBFS = [];
const t = new Tree();
t.root = new Node('a');
t.root.add('b');
t.root.add('d');
t.root.children[0].add('c');
t.BFS(node => lettersBFS.push(node.data));

console.log(lettersBFS)
