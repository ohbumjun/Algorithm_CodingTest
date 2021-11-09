// 아나그램 검사 코드
const compMaps = (map1,map2) => {
    // console.log(map.size) // Map.size : key의 개수, 종류 --> 아나그램이라면, key size는 같아야 한다 
    // 1. 키 개수가 다르다면 
    if(map1.size !== map2.size) return false ;
    for(let [key,val] of map1){
        // 2. 키가 다르다면 or 3. 키값의 val이 다르다면
        if(!(map2.has(key)) || map2.get(key) !== val ) return false;
    }
    return true
}
// Map 버전
const solution = (S,T) => {
    // S가 더 긴거, T가 짧은 거 
    let res = 0;
    let tH = new Map();
    let sH = new Map();
    // map 세팅 
    for(let x of T){
        if(tH.has(x)) tH.set(x,tH.get(x)+1)
        else tH.set(x,1)
    }
    // 만약 길이가 3이면, 2개는 미리 세팅해둔다 : 슬라이딩 윈도우 --> lt, rt
    // lt 빼고, rt 추가 -> 오른쪽으로 차근차근 이동시키기 
    let len = T.length - 1 
    for(let i = 0 ; i < len ; i++){
        if(sH.has(S[i])) sH.set(S[i],sH.get(S[i])+1)
        else sH.set(S[i],1)
    }
    // 이제 슬라이딩 윈도우 돌기
    let lt = 0;
    for(let rt = len; rt < S.length; rt++){
        // 추가 
        if(sH.has(S[rt])) sH.set(S[rt],sH.get(S[rt])+1)
        else sH.set(S[rt],1)
        // 비교 
        if(compMaps(sH,tH)) answer += 1
        // lt 빼기 
        sH.set(S[lt], sH.get(S[lt]) - 1)
        if(sH.get(S[lt]) == 0) sH.delete(S[lt]) // key값 삭제 
        lt += 1
    }
    return res;
}

let str1 = 'bacaAacba'
let str2 = 'abc'
console.log(solution(str1,str2))
