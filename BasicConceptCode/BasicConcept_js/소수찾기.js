// 1부터 100까지 사이의 소수
let 소수 = []
let 소수판별 = true

for(let i = 2; i < 100; i++){
    for(let j = 2; j < i; j++){
        if( i % j == 0)
            소수판별 = false
    }
    if(소수판별)
        소수.push(i)
    
    소수판별 = true; //  소수판별 초기화 
}

console.log(소수)

