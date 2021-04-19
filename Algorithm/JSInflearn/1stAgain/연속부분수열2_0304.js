function solution(a, b,arr){

    let answer = 0 , sum = 0 , st = 0;

    /*
    매번 원소를 추가할때마다, 해당 원소에서, stP까지 가변서, 해당 원소를 포함하는 새로운 부분수열들을 더해간다 
    1   3   1   2   3

    1

        3
        1,3
            1
            3,1
            1,3,1
    */

    // 이문제의 핵심은, 중복을 제거하는 것
    // 즉, 같은 {1} 이라는 애를 계속 같이 더하면 안된다는 것이다

    // 아래의 코드의 깔끔함 1 : for 문 안에 ed를 넣어준 것
    // 아래의 코드의 깔끔함 2 : arr[st++] 이렇게 후위증감 사용

    for(let ed = 0 ; ed < arr.length; ed++){
        sum += arr[ed]
        while(sum > b){
            sum -= arr[st++]
        }
        answer += ( ed - st + 1) 
    }

    return answer;
}

let a = 5 ;
let b = 5 ;
let c = [ 1,3,1,2,3 ]
console.log(solution(a, b,c));