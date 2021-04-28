const solution = (num) => {
    let ans = ''
    const dfs = (n) => {
        if(n == 0) return
        dfs(parseInt(n/2))
        ans += String(n%2)
    }
    dfs(num)
    return ans
}


console.log(solution(11))

