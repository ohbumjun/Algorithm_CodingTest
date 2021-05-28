//https://webigotr.tistory.com/247


// 에라토스 테네스의 체 : n보다 작은 수 중에서 소수 출력
function prime_list(n){
    let sieve = [ ]

    for(let i = 2; i < n; i++){
        sieve.push(true);
    }

    let m = parseInt(n ** 0.5 , 10)
    // parseInt :  문자열 인자를 특정 진수의 정수로 반환하기 

    for(let i =2 ; i < m + 1; i++){
        if(sieve[i] == true){
            // 해당 배수들을 모두 !! false로 바꾼다 
            for(let j = i  + i ; j < n; j+= i){
                sieve[j] = false;
            }
        }
    }

    // 소수 목록 산출
    let 소수목록 = []
    for( let i = 2; i < n; i++ ){
        if( sieve[i] == true)
            소수목록.push(i)
    }
    return 소수목록
}





function solution(numbers) { 
    var answer = 0; // numbers를 배열로 변환하고 내림차순으로 정렬 
    let a = numbers.split('').sort((a,b)=>b-a); // 최댓값 
    let N = Number(a.join('')); 
    // 에라토스 테네스의 체로 소수 구하기 
    let arr = makePrimeNum(N); 
    for(let i=2; i<=N; i++){ 
        // 소수가 아니면 패스 
        if(arr[i] == false) continue; 
        // 소수면 해당 숫자를 문자열로 바꾸고 배열로 변환 
        let temp = i.toString().split(''); 
        // numbers에 해당 하는 값을 돌면서 temp에도 있으면 temp에서 삭제 
        for(let cn of a){ 
            let idx = temp.indexOf(cn); 
            if(idx > -1) // 해당 값이 존재한다면
                temp.splice(idx,1);   // temp에서 해당 값을 제거한다  ex. [2,3]에서 2 제거 = [3]
        } 
        // temp.length 가 0이면, numbers에 모두 있는 숫자이므로 answer++
        // 즉, 일반적으로, 모든 수를 조합한 다음에 ! 소수를 제거하는 방식을 사용한 거라기 보다는
        // 주어진 numbers 도 하나하나쪼개고, 소수 목록들도 하나하나 쪼개서, 쪼갠 소수 목록들이 
        // 쪼개진 numbers 에 있다는 것은, numbers내의 조합들로, 해당 소수가 만들어질 수 있다는 것.
        if(temp.length == 0) answer++; 
    } 
    return answer; 
}

// 에라토스 테네스의 체 다른 버전
function makePrimeNum(N){
    let arr = []
    for(let i = 2; i <= N; i++){
        if(arr[i] == false) continue;
        for(let k = i + i ; k <= N ; k+= i){
            arr[k] = false
        }
    }
    return arr
}
