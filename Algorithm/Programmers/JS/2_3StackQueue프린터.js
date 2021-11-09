
/*   < 처음 답안 함수 : 시간 부족 문제 해결 못함 > -------------------------------------
function solution(priorities, location) {
    
    // priorities를 그대로 큐로 사용한다
    
    // 현재 인쇄된 횟수 
    let NumberPrinted = 0;
    
    // location에 있는 애의 위치를 계속 확인해야 한다 
    // 현재 배열로 부터, 값, + idx 쌍이 하나의 원소로 묶이는 object 배열 생성하기 
    let ElementObject = []
    priorities.forEach( (priority, index ) => {
        ElementObject.push({ value : priority, index : index })
    })
    
    while(1){
        // 1. pop 하고
        let tempNum = ElementObject.shift()

        // 2. 모든 배열 돌아서 우선순위 확인하고
        for(let i =0 ; i < ElementObject.length; i++){
            if(ElementObject[i].value > tempNum.value ){
                ElementObject.push(tempNum)
                break;
            }
            if( i == ElementObject.length - 1 ){
                // 여기까지 왔다는 것은 해당 문서보다 중요한 문서가 없다는 것
                // number를 1 증가시키고
                    NumberPrinted += 1
                // 만약 현재 뽑은 문서의 index가 우리가 목표한 location이라면 number를 return
                    if(tempNum.index == location )
                        return NumberPrinted
            }
        }
    }

}

*/




/* 시간 문제 해결방법 : for대신에 find 함수 사용 */
function solution(priorities, location) {
    
    // priorities를 그대로 큐로 사용한다
    
    // 현재 인쇄된 횟수 
    let NumberPrinted = 0;
    
    // location에 있는 애의 위치를 계속 확인해야 한다 
    // 현재 배열로 부터, 값, + idx 쌍이 하나의 원소로 묶이는 object 배열 생성하기 
    let ElementObject = []
    priorities.forEach( (priority, index ) => {
        ElementObject.push({ value : priority, index : index })
    })
    
    while(1){
        // 1. pop 하고
        let tempNum = ElementObject.shift()

        // 2. 모든 배열 돌아서 우선순위 확인하고 ( for문으로 하면, 시간 초과가 걸린다 )
        const result = ElementObject.find(( element) => element.value > tempNum.value)
        
        if( result ){
            // 뒤에 우선순위가 더 높은 값이 존재한다면, 아무것도 하지말고 그저 push
            ElementObject.push(tempNum)
        }else{
            // 그 외의 경우에는, 더 높은 값이 없다면, 해당 요소 +1 시키고, 우리가 목표한 location에 해당하는 index라면 return 
            NumberPrinted += 1
            if(tempNum.index == location )
                return NumberPrinted

        }
      
    }

}