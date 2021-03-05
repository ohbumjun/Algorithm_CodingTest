function solution(progresses, speeds) {
    var answer = [];
    let result = 0;
    
    while(progresses.length != 0){
        
        // result 값읓 초기화 해준다
        result = 0 ;
        
        // 모든 진행 사항들에 대해서 +1을 해준다
        progresses.forEach((progress, index) => {
            if(progresses[index] < 100)
                progresses[index] += speeds[index]
        })
        
        // 100 이상인 수들을 뽑아서 넣어준다
        for(let i = 0 ; i < progresses.length ; ){
            if( progresses[i] >= 100 ){
                
                // 작업 배열과 속도 배열에서 해당 값들을 제거해준ㄷ 
                progresses.shift()
                speeds.shift()
                result += 1
            }else{
                break;
            }
        }
        
        // result 값을 answer 앞에 push 해준다
        if( result != 0)
            answer.push(result)
    }
    
    return answer;
}