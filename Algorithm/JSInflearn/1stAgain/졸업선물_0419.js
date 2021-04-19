const solution = (product) => {
    let N = 5 // 학생 수 
    let M = 28 // 예산 
    let res = 0; 
    // 0) 가격을 기준으로 모두 정렬하기 ( 이게 핵심 point --> 먼저 모두 정렬해둔다 )
    // 1) for 문을 돌면서, 각 학생에 대해서 우선, 상품가격을 1/2로 해준다 
    // 2) 남아있는 상품들을, 이제 담기 --> 선물할 수 있는 최대 학생수 == 가장 저예산 부터 담기
    product.sort((a,b) => (a[0]+a[1]) - (b[0]+b[1]))
    let len = product.length
    for(let i = 0 ; i < len; i++){
        let totC = 0, cnt = 1;
        totC += (product[i][0]/2 + product[i][1])
        for(let j = 0 ; j <len ; j++ ){
            if(j != i && product[j][0] + product[j][1] + totC <= M ){
                totC = totC + product[j][0] + product[j][1]
                cnt += 1
            }
        }
        res = Math.max(cnt,res)
    }

    return res
}

let s = [[6,6],[2,2],[4,3],[4,5],[10,3]]

console.log(solution(s)); 