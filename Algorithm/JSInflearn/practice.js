const solution = (arr) => {
    // 자신을 기준으로 왼쪽을 본다
    // 자신보다 작으면서, 가장 큰 숫자를 찾고, 그 해당 숫자의 dp[i] 값 + 1을 해준다
    const len = arr.length;
    let answer = 0;
    let dp = Array(len).fill(0)
    for(let i = 0 ; i < len; i++){
        let maxElem = 0 , maxVal = 0;
        for(let j = 0; j < i ; j++){
            if(arr[j] < arr[i] && arr[j] > maxElem){
                maxElem = arr[j]
                maxVal = dp[j]
            }
        }
        dp[i] = maxVal + 1
        answer = Math.max(dp[i],answer)
    }
    return answer
}

const arr = [5 ,3 ,7 ,8 ,6 ,2 ,9 ,4]
console.log(solution(arr))
