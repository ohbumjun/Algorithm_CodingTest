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

    constructor(){

        this.root = null;

    }

    DFS(fn){

        
        if(this.root == null) return;

        const unvisitedList = [this.root];

        while(unvisitedList.length != 0 ){

            // shift : 배열 첫번째 요소 제거하기
            const current = unvisitedList.shift()

            unvisitedList.unshift(...current.children)
            // 앞에다가 넣어주는 것이 

            fn(current);
            /*
            a
            b d 
            */
        }

        
    }
}

const lettersDFS = [];
const t = new Tree();
t.root = new Node('a');
t.root.add('b');
t.root.add('d');
t.root.children[0].add('c');
t.DFS(node => lettersDFS.push(node.data));

console.log(lettersDFS)