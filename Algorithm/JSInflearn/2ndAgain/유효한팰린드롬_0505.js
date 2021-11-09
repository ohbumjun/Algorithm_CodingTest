

function solution(s ){
    let res = ""
    s = s.toLowerCase().replace(/[^a-z]/g,'') // 알파벳 소문자만 남게 한다 --> ^ : not 
    if(s.split('').reverse().join('') == s){res = "YES"}
    else{ res = "NO"}
    return res
}

let s = 'found7, time: study; Yduts; emit, 7Dnuof'

console.log(solution(s));