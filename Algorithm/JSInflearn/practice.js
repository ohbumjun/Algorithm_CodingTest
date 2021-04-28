const solution = (arr) => {
    const max = 259;
    const n   = 5;
    // 결국은, 얘를 태울 것인가 말것인가 
    let ans = 0;
    const dfs = (idx,sum) => {
        if(idx == arr.length){
            if(sum <= max){
                console.log("sum", sum)
                ans = Math.max(sum,ans)
                return
            }
        }else{
            // 선택
            dfs(idx+1,sum + arr[idx])
            // 선택 x
            dfs(idx+1,sum)
        }
    }
    dfs(0,0,0)
    console.log(ans)
}

const arr = [81,58,42,33,61]
solution(arr)
