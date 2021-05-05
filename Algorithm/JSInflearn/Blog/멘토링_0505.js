const solution = (arr) => {
    let N = 4 // 학생 수 
    let M = 3 // 테스트 번째 수
    let ans,mentor,mentee,res = 0;

    // 4중 for문 -> i를 멘토 j를 멘티.로 설정하여 , 각 테스트에서 i 점수가 j 점수보다 낮은지를 확인하면 된다 
    for(let i = 0 ; i < N ; i++){ // 멘토 
        for(let j = 0 ; j < N; j++){ // 멘티 
            ans = -1
            mentor = -1
            mentee = -1
            for(let k = 0; k < M; k++){ // 테스트 번째수 
                for(let s = 0 ; s < N; s++){ // 학생 번호 
                    // 멘토 등수와 같다면 
                    if( s == i ){mentor = arr[k][s]}
                    // 멘티 등수와 같다면 
                    else if( s == j){mentee = arr[k][s]}
                    if(ans == -1 && mentor < mentee){ans = 1}
                }
            }
            if(ans == 1) res += 1
        }
    }
    
    return res
}

let s = [[3,4,1,2],[4,3,2,1],[3,1,4,2]]

console.log(solution(s)); 