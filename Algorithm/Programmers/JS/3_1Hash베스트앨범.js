// link : https://one-it.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Hash-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94

/*
< Map  함수 >
Map() 은 자바스크립트의 key-value 페어(pair) 로 이루어진 컬렉션
key 를 사용해서 value 를 get, set 할 수 있음
key 들은 중복될 수 없음: 하나의 key 에는 하나의 value 만
key 로 사용할 수 있는 데이터형: string, symbol(ES6), object, function >> number 는 사용할 수 없음에 주의!


< Find 함수 >
형식 : arr.find(callback(element[, index[, array]])[, thisArg])

원리 : 배열에서 특정 값을 찾는 조건을 callback 함수를 통해 전달하여,

조건에 맞는 값 중 첫번째 값을 리턴합니다.

만약 배열에 조건을 만족하는 값이 없으면 undefined를 리턴합니다.

파라미터 :
callback(element, index, array) 함수

조건을 비교할 callback 함수이고, 다음 3개의 파라미터가 전달됩니다.

callback 함수에서 사용자가 테스트할 조건을 정의하고,

만약 배열의 값이 조건에 부합하여 true를 리턴하면,

해당 배열의 값이 find() 함수의 리턴 값이 됩니다.

조건에 부합하는 값을 찾으면, 그 이후의 배열값은 테스트되지 않습니다.

element : 현재 처리중인 배열의 element입니다.
index : 현재 처리중인 배열의 index입니다. (optional)
array : find() 가 호출된 배열입니다. (optional)
thisArg (optional)

callback을 실행할 때 this로 사용할 객체입니다.


*/

const solution = (genres,plays) => {
    let answer=[];
    let totalPlayMap = new Map();
  
  // 장르별, 총 노래 재생 수를 저장해두는 Object 구하기 
  // Reduc 함수 사용법 >  배열.reduce((누적값, 현잿값, 인덱스, 요소) => { return 결과 }, 초깃값);
    let totalPlayObj = genres.reduce(((acc,item,idx) => {
  // acc는 배열이 아니라, 객체이다 ( 맨 끝에 , 초기값을 {}로 세팅했기 때문이다 ) 
  // item은 현재 genre 상에서의 value이다 
    if(!acc[item]) {acc[item] = plays[idx];}
      else {acc[item] = acc[item] + plays[idx];}
      return acc;
    }),{})
    
    // 재생 순서 별 정렬하기 
    let playArr = [...Object.values(totalPlayObj)].sort((x,y) => y - x) // 내림차순 정렬된 재생 수 Array
  
    
    // Map 함수 형태 만들기 
    for(let item of playArr){
      // find 함수 : 배열의 특정 값 찾기
      // key : 특정 장르를 의미한다 
        let key = Object.keys(totalPlayObj).find(key => totalPlayObj[key] === item);
        
      // 모든 값을 0으로 채운 배열을 마련한다 
      let arr=[];
      arr.length = genres.length;
      arr.fill(0);
      for(let i=0;i<arr.length;i++){
          // ex. genre가 poppin 인 애들의 value들 만을 arr 라는 배열에 넣는다
        if(genres[i] === key){arr[i]=plays[i]}
      }
      totalPlayMap.set(key,arr); // 순서를 보장해주는 데이터 타입이면서 Hash형태인 Map
    }
  
    for (let [key,value] of totalPlayMap){
      const arr = [...value].sort((a,b) => b - a);
      for(let item of arr){
                      // item == 0 이라는 것은, 해당 음악 장르에 해당하는 노래가 없다는 것 
              // indexOf(item)이 2라는 것은, 해당 음악 장르에 해당하는 노래를 2개 이미 선택했다는 것 
        if(item === 0 || arr.indexOf(item) === 2){break}
        else {
          answer.push(value.indexOf(item));
            // / 해당 내용은 비워준다... 굳이 ?? 왜냐하면, 재생수가 동일한 음악들의 경우, 같은 index를 answer에 push할 수 있다는 것이다. 그래서 한번 처리된 value아이템은 null로 바꿔주어야 한다
          value[value.indexOf(item)] = null;
        }
      }
    }
    return answer;
  }