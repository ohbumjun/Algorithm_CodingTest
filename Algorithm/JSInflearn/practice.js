function solution(m, songs){
    // 사실 매번 요소가 새롭게 추가될 때마다 , 현재 부분수열 첫번째 원소 ~ 차례대로 부분 수열 마지막 원소 까지의 숫자가 , 경우의 수로 더해진다
    // 즉, 기존 부분수열 합 + 새로운 원소 <= M : lastLen - firstLen + 1 을 해주면 된다

    // 단, > M 이라면, 합이 <=M이 될때까지 firstLen , 즉, 앞의 포인터 위치를 뒤로 옮겨주고, <= M 이 되는 그 순간에 다시 위의 과정 처럼 더해주면 된다r
    let sumSong = 0 ;
    let answer  = 0
    let lt = 0;

    for(let rt = 0 ; rt < songs.length; rt ++ ){
        sumSong += songs[rt]
        while(sumSong > m)
            sumSong -= arr[lt++]
        answer += (rt - lt + 1)
    }

    return answer

    
}

let a = 5 ;
let b = 5 ;
let arr = [ 1,3,1,2,3 ]
console.log(solution(a,arr))