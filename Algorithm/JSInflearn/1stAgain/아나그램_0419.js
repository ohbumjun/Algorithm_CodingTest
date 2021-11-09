// Map 버전
function solution(str1,str2){
    let res = "YES";
    let sH = new Map();

    // 세팅 
    for(let x of str1){
        if(sH.has(x)) sH.set(x,sH.get(x)+1) 
        else{sH.set(x,1)}
    }

    // 공통된 애들 상쇄시키기
    for(let x of str2){
        // 1.아예 없거나 or 2.개수가 일치하지 않거나
        if(!(sH.has(x)) || sH.get(x) == 0 ) return "NO"
        // 상쇄
        sH.set(x,sH.get(x)-1)
    } 
    
    return res 
}

let a = 10 ;
let b = 3 ;
let str1 = 'abaCC'
let str2 = 'Caaab'
console.log(solution(str1,str2))

// 일반 obj 버전  ----
/*
function solution(str1,str2){
    str1 = str1.split(''); str2 = str2.split('')
    let dict1 = {}, dict2 = {}
    let res = 1, keys ;
    for(let i=0;i<str1.length;i++){
        if(str1[i] in dict1){dict1[str1[i]] += 1}
        else{dict1[str1[i]] = 1}
    }
    for(let i=0;i<str2.length;i++){
        if(str2[i] in dict2){dict2[str2[i]] += 1}
        else{dict2[str2[i]] = 1}
    }
    keys = Object.keys(dict1)
    for(let key of keys){
        if( !(key in dict2) || (dict1[key] != dict2[key])){ 
            res = -1
            break
        }
    }
    return res == 1 ? true : false;
}

let a = 10 ;
let b = 3 ;
let str1 = 'abaCC'
let str2 = 'Caaab'
console.log(solution(str1,str2) ? "YES" : "NO")
*/