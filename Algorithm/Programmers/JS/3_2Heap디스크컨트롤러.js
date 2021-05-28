function solution(jobs){
    /*

    링크 : https://kyun2da.github.io/2020/07/21/diskController/

        하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다. 라고 써있으므로 먼저 요청의 시간순으로 jobs를 정렬해야합니다.
    그러나 요청의 시간순으로 처리하면 문제의 예처럼 최소시간을 보장하지 못합니다. 여기서 필요한 것이 중간단계의 우선순위 큐입니다.
    우선순위 큐에는 해당작업을 처리하는동안 요청이 오는 모든 jobs들을 넣어줍니다. 예를 들어 0초부터3초까지의 작업을하는 하나의 작업이 있다고하면 0,1,2,3초에 요청이 온 모든 작업을 우선순위 큐에 넣어줍니다.
    그리고 작업이 끝나면 우선순위 큐에있는 작업중 가장 처리시간이 작은 작업부터 실행해줍니다. 이것이 최소시간을 만족하는 방법이기 때문입니다.
    이런식으로 작업은 jobs의 작업들이 모두 끝날때 까지 계속됩니다.
    마지막으로 주의할 점은 우선순위 큐가 다 비고나서 작업이 아직 남아있다면 jobs의 첫번째 배열에있는 작업을 실행해주면됩니다. 즉 요청의 시간순으로 다시 실행해 주면 된다는 뜻입니다.
    */
        let answer = 0,
            j = 0,
            time = 0;
    
        jobs.sort((a,b)=>{return a[0] - b[0]}) // 요청시간 기준 정렬
    
        // 중간 과정의 우선순위 큐
        const priorityQueue = []
        while( j < jobs.length || priorityQueue.length != 0){
            // 작업 목록에 작업이 남아있고
            // 진행 시간 중에, 요청 시간이 시작되는 작업들을 넣는다 
            if( jobs.length > j && time >= jobs[j][0]){
                priorityQueue.push(jobs[j++])
                
                // 우선 순위 큐에 모두 넣고나면
                // 해당 작업들을 , 소요시간이 작은 것 기준으로 정렬한다 
                priorityQueue.sort((a,b) => {
                    return a[1] - b[1];
                })
                continue;
            }
            
            // 해당 우선순위 큐에 들어간 작업들을 처리한다 
            if( priorityQueue.length != 0){
                // 현재 이 작업이 끝나는 시간에서, 요청 시간을 빼야지만, 순수하게 해당 작업이 걸리는 시간이 계산된다 
                time += priorityQueue[0][1]
                answer += time - priorityQueue[0][0] 
                priorityQueue.shift()
            }else{
                time = jobs[j][0]
            }
        }
    
    return parseInt(answer/jobs.length)
    
    }