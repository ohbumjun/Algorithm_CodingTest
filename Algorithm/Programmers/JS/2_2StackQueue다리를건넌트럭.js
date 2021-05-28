function solution(bridge_length, weight, truck_weights) {
    // answer : 걸린 시간
    let answer = 0;
    
    // queue : 현재 다리 상태
    let queue = []
    
    // queue : 현재 다리 쿠게
    let queueSum = 0;
    
    /* 1. 초기 작업 */ 
    // Queue의 길이는, 다리 길이로 하고, 하나하나를 0으로 초기화
    for(let i = 0 ; i < bridge_length; i++){
        queue.push(0)
    }
    
    // now_truck : 현재 다리를 지나가는 트럭
    let now_truck = truck_weights.shift()
    
    // 큐에 트럭을 넣고, 다리를 앞으로 한칸씩 땡긴다
    // 왼쪽에서 오른쪽으로 다리는 건너는 과정을 생각하면 된다. 
    queue.unshift(now_truck) // 맨왼쪽에 하나 넣고 
    queue.pop()// 맨 오른쪽은 뺀다
    // 앞에 넣고, 뒤에 빼고를 한번씩하게 되면, 이는 곧, 오른쪽으로 값을 하나 이동시키는 것과 같은 원리이다 
    
    // 다리 무게 증가
    queueSum += now_truck
    
    // 시간 증가 
    answer ++;
    
    /* 2. 중간 작업 */
    // 쉬지 않고, 큐에 트럭을 넣거나, 다리를 건너기 때문에
    // queueSum이 0이 되면, 모든 트럭이 지나간 것이다
    while(queueSum !=0 ){
        // 다리에 있는 트럭을 이동 시킨다( 오른쪽으로 이동 : pop 시켜서 제거)
        queueSum -= queue.pop()
        
        // 일단 다리를 안건넌 트럭을 하나 뺀다
        now_truck = truck_weights.shift();
        
        // 다리에 들어갈 수 있으면, 큐(다리)에 트럭 넣고, 무게 증가
        if( now_truck + queueSum <= weight){
            queue.unshift(now_truck)
            queueSum += now_truck
        }else{
            // 다리에 들어갈 수 없으면, 0을 넣고 , 뺏던 거를 다시 트럭집단에 고스란히 넣어준다
            queue.unshift(0);
            truck_weights.unshift(now_truck)
        }
        answer++
    }
    return answer
}