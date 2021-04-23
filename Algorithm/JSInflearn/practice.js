const bubble = (arr) => {
    // 가장 큰 것을 순차적으로 뒤로 보내는 알고리즘
    // 한번 정렬 때마다, 가장 큰 수가 뒤로 위치하게 된다
    let len = arr.length
    for(let i = 0 ; i < len-1; i++ ){ // 바꾸는 횟수
        for(let j = i; j < len - 1 - i; j++ ){
            if(arr[j] > arr[j+1]){
                [arr[j],arr[j+1]] = [arr[j+1],arr[j]]
            }
        }
    }
    return arr
}
const selection = (arr) => {
    // 선택 정렬 : 자기 기준 오른쪽에서 가장 작은 값으로 대체해간다
    let len = arr.length
    for(let i = 0 ; i < len - 1; i++){
        let idx = i, minV = arr[i]
        for(let j = i + 1; j < len ; j++){
            if(arr[j] < minV){
                minV = arr[j]
                idx = j 
            }
        }
        [arr[idx],arr[i]] = [arr[i],arr[idx]]
    }
    return arr
}
const insertion = (arr) => {
    let len = arr.length,j;
    // 자기 기준 왼쪽으로 위치 찾아가기
    for(let i = 1; i < len; i++){
        let tmp = arr[i]
        for(j = i-1; j >= 0; j--){
            if(arr[j]>tmp)arr[j+1] = arr[j]
            else break;
        }
        [arr[i],arr[j+1]] = [arr[j+1],arr[i]]
    }
    return arr
}

const arr = [5 ,7 ,11 ,13 ,15 ,23]
console.log(insertion(arr))