// https://exercism.io/my/solutions/56a5c8834d86434ab70ae827da1808fd

class Node{
    constructor(value, next = null ){
      this.value = value
      this.next  = null
      this.prev  = null
    }
  }
  
  export class LinkedList {
    constructor(){
      this.head = null;
      this.tail = null;
      this.size = 0;
    }
  
    // remove element from the back, return value in the tail
    pop(){
      let value = this.tail.value
      
      // tail이 없다면
      if(!this.tail){
        return null
      }
  
      // 기존 연결리스트 상에서 연결 해제
      this.tail = this.tail.prev;
      this.tail.next = null
  
      this.size -= 1
      return value;
    }
  
    // add data in the tail
    push(value){
      
      let newNode = new Node(value)
  
      // head와 tail이 없다면, 즉, 아예 노드가 존재하지 않았다면
      if(!this.head && !this.tail){
        this.head = newNode;
        this.tail = newNode;
      }
  
      newNode.prev = this.tail
      this.tail.next =  newNode;
      this.tail = newNode;
  
      this.size += 1
  
      return this
  
    }
  
    // remove element in the head
    shift = () => {
      let value = this.head.value;
      // if head does not exist
      if(!this.head ){
        return null
      }
      
  
      this.head = this.head.next;
      if(this.head){
        this.head.prev = null;
      }
  
      this.size -= 1
  
      return value
    }
  
  
    // add element in the head
    unshift = (value) => {
      let newNode = new Node(value)
  
      // this.head가 없다면
      if(!this.head  && !this.tail){
        this.head = newNode;
        this.tail = newNode;
      }
  
      // add element
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode;
  
      this.size += 1
  
      return this
    }
  
    count = () => {
      return this.size;
    }
  
    delete = (value) => {
      let node = this.head;
      let previous = undefined;
  
      // 맨 앞의 값이 찾는 값을 갖고 있었을 때
      if( node && node.data == n ){ return this.shift()}
  
      while( node ){
          if( node.data == n ){
            previous.next = node.next ? node.next : null;
          }
          previous = node;
          node = node.next;
      }
  
    }
  }
  