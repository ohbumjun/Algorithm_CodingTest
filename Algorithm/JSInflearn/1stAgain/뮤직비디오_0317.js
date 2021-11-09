/*
원리는 다음과 같다.

최소로 가능한 dvd 길이는 9
최대로 가능한 dvd 길이는 45

이제 이 사이에서 
m개의 dvd로 , 모든 음악들을 담을 수 있는
최소의 dvd 길이는 구하면 되는 것이다

여기서 중요한 것은, 이분검색으로 구하되
m-1개로 담아도 괜찮다
그냥 1개 남기면 어떻냐

단, m개로 담는 dvd길이를 찾더라도
우리는 이분검색을 통해
더 최적의 답을 향해 나아가야 한다 

*/

// 해당 dvd 길이로 담을 수 있는 장수
function count(songs, capacity){
    // cnt 를 1로 시작하는 것이 중요하다
    // 그래야만, for 문을 다 돌고나서
    // 값이 남아있는 경우를 simple하게 처리가능
    // 즉, 그냥 바로 cnt +=1 을 해주면 된다는 것이다 
    let cnt = 1, sum = 0;
    for(let x of songs){
        if(sum + x > capacity){
            cnt += 1
            sum = x
        }else{
            sum += x 
        }
    }
    return cnt
}

function solution( m, songs ){

    let answer ;
    let lt = Math.max(...songs)
    let rt = songs.reduce((acc,val) => acc + val )
    while(lt <= rt){
        let mid = parseInt((lt + rt) / 2)
        if(count(songs, mid) <= m){
            answer = mid
            rt = mid - 1
        }else{
            lt = mid + 1
        }
    }
    return answer
}

let a = 9 ;
let m = 3 ;
let arr = [ 1,2,3,4,5,6,7,8,9 ]
let answer = 0
console.log(solution(3, arr));