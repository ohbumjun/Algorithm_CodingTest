// https://exercism.io/my/solutions/3835f4f907b0425e99137288bfcb1603


export class List {

    // List 자체가 이미 배열이고, 그 안에 values 라는 속성을 넣어야 한다.
    constructor(values) {
      this.values = values || [];
    }
  
    append(list) {
      return new List([ ...this.values , ...list.values])
    }
  
    concat(listOfLists) {
      let newList = new List(this.values);
  
      for(list of listOfLists){
        // newList = newList.append(list)
        newList = [...newList, ...list]
      }
  
      return newList
    }
    /*
    Predicate : refers to function which
    returns either true or false
  
    ex. const greaterThan10 = value => value > 10;
    console.log(greaterThan10(11)) >> result : True
  
    */
  
    filter(FilterFunc) {
      let newList = new List(this.values)
      for(elem of newList){
        if(FilterFunc(elem)) newList = [...newList, elem]
      }
      return newList
    }
  
    map(MapFunc) {
      let newList = new List()
      for(let i = 0 ; i < this.length() ; i++){
        newList = [ ...newList , MapFunc(this.values[i]) ]
      }
  
      return newList
    }
  
    length() {
      // Array.length 
      return this.values.length
    }
  
    foldl(reduceFunction, initVal) {
      let curVal = initVal;
      for(let i = 0 ; i < this.length() ; i++ ){
        curVal = reduceFunction(curVal, this.values[i])
      }
      return curVal
    }
  
    fold1Func(reduceFunc, initVal){
      let curVal = initVal
      for(let i = this.length() ; i > -1 ; i++ ){
        curVal = reduceFunc(curVal, this.values[i])
      }
      return curVal
  
    }
  
  
    reverse() {
      let newList = new List()
      for( let i = this.length() ; i > -1 ; i++ ){
        newList = [...newList, this.values[i]]
      }
      return newList
    }
  }
  