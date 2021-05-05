const solution = (product) => {
    let n = 5, m = 28; answer = 0;
    product.sort((a,b) => (a[0]+a[1]) - (b[0]+b[1]))
    // 각 상품을 1/2 해준 다음
    // 그 이후, 상품을 차례대로 담는 경우 생각하기
    for(let i = 0 ; i < product.length; i++){
        let money = m - (product[i][0]/2 + product[i][1])
        let cnt   = 1
        for(let j = 0 ; j < n; j++){
            if(j != i && money - (product[j][0] + product[j][1]) >= 0 ){
                money -= (product[j][0] + product[j][1])
                cnt += 1
            }
        }
        answer = Math.max(answer,cnt)
    }
    return answer
}

let s = [[6,6],[2,2],[4,3],[4,5],[10,3]]
console.log(solution(s)); 