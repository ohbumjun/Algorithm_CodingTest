function solution(a, b,arr){

    let answer = 0 , sum = 0 , st = 0;

    // 우선 계속 새로 추가해간다.
    // 그리고 추가 이후, 조건에 만족하면 ed - st + 1 을 해준다.
    // 만약 조건에 만족하지 않으면 ?? 조건에 만족할때까지 st를 빼가고
    // 조건에 만족하게 되었을 때 그때 또 다시 ed - st + 1을 해준다

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