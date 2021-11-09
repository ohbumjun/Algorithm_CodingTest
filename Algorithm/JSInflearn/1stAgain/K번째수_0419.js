const solution = (n,k,arr) => {
    // 중복을 제거해야 함 : Set 이용 
    let ans;
    let tmp =  new Set(arr);
    for(let i = 0 ; i < n-2 ; i++){ // 3개 뽑는 것인데 n-2 이렇게 해야지, n으로 하면 안되지 않나 ?? 상관 x 
        for(let j = i+1 ; j < n-1; j++){ // 왜 상관 x ? 범위 조건으로 인해서, 알아서 멈추기 때문이다 
            for(let k = j+1 ; k < n; k++){
                tmp.add(arr[i]+arr[j]+arr[k])
            }
        }
    }
    ans = Array.from(tmp).sort((a,b) => b - a)
    return ans[k-1]
}

let s = [13,15,34,23,45,65,33,11,26,42]

console.log(solution(10,3,s)); 