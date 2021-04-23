const selection = (arr) => {
    // 자기 기준 오른쪽 최소값을 찾아서, 자기와 바꿔준다 
    let len = arr.length
    for(let i=0;i<len-1;i++){
        let idx = i
        for(let j=i+1;j<len;j++){
            if(arr[j]<arr[idx]) idx = j 
        }
        [arr[i],arr[idx]] = [arr[idx],arr[i]]
    }
    return arr
}

const bubble = (arr) => {
    // 원리 : 가장 큰 것을 오른쪽으로 
    let len = arr.length;
    for(let i =0;i<len-1;i++){
        let idx = i;
        let maxV = 0;
        let j = 0
        for(j =0;j<len-1-i;j++){
            if(arr[j] > arr[j+1]){
                [arr[j],arr[j+1]]=[arr[j+1],arr[j]]
            }
        }
    }
    return arr
}
const insertion = (arr) => {
    // 자기 기준 왼쪽은 이미 정렬, 왼쪽에서의 자기 위치 찾아 들어가기
    let len = arr.length;
    for(let i = 1; i < len;i++){
        let tmp = arr[i] , j ;
        for(j = i-1; j >= 0;j--){
            if(arr[j]>tmp) arr[j+1] = arr[j]
            else break 
        }
        // 1 4 6 9 5
        // 1 4 6 6 9 : 4에 j가 있음
        arr[j+1] = tmp
    }
    return arr;
}

let arr = [13,5,11,7,23,15]

console.log(insertion(arr)); 