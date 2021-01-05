function solution(operations) {
    
    let queue = []
    // 넣어줄 때마다 , sort를 한다 
    for(let i = 0 ; i < operations.length; i++ ) {
        let Order = operations[i].split(" ")
        // 입력 명령어라면
        if(Order[0] == "I"){
            queue.push(Number(Order[1]))
            // sort 
            queue.sort((a,b) => { return b - a })
            console.log("insert", queue)
        }else if( Order[1] == "1" ){
            // 최댓값 삽입  : 맨앞에 꺼 빼기 
            queue.shift()
            console.log("Max Delete", queue)
        }else if( Order[1] == "-1" ){
            // 최소값 삭제 : 맨 뒤에꺼 빼기
            queue.pop()
            console.log("Min Delete", queue)
        }
    }
    
    let MaxVal = queue.shift()
    if( MaxVal == null)
        MaxVal = 0
    let MinVal = queue.pop()
    if( MinVal == null)
        MinVal = 0
    
    return [MaxVal, MinVal]
    // return [queue.shift() == null ? 0 : queue.shift(), queue.pop() == null ? 0 : queue.pop()]
}