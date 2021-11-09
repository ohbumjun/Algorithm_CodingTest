

function solution(str ){
    let res = 0
    str.split('').forEach(s => {
        if(!isNaN(s)){
            res = res * 10 + Number(s)
        }
    })
    return res
}

let s = 'g0en2T0s8eSoft'

console.log(solution(s));