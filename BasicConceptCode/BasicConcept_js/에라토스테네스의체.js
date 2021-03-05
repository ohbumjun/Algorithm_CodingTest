// https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
function prime_list(n){
    let sieve = [ ]

    for(let i = 2; i < n; i++){
        sieve.push(true);
    }

    let m = parseInt(n ** 0.5 , 10)
    // parseInt :  문자열 인자를 특정 진수의 정수로 반환하기 
    // n의 최대약수가 sqrt(n) 이하이므로 

    for(let i =2 ; i< m + 1; i++){
        if(sieve[i] == true){
            // 해당 배수들을 모두 !! false로 바꾼다 
            for(let j = i  + i ; j < n; j += i){
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

console.log(prime_list(10001))