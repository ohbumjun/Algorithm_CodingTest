

function solution( n , arr ){
    function initArr(n, arr){
    
        let distArr = Array.from(Array(n+1), () => Array(n+1).fill(0))
        for(let [a,b] of arr){
            distArr[a][b] = 1
        }
        return distArr
    }
    
    function DFS(node){
        // n, res는 scope 상 위에 존재하게 해야 
        if(node == n){
            res += 1
            return 
        }else{
            // 해당 배열 탐색 
            for(let i = 1; i < n + 1; i++ ){
                if( distArr[node][i] == 1 && chList[i] == 0 ){
                    chList[i] = 1
                    DFS(i)
                    chList[i] = 0
                }
            }
        }
    }

    let numRoad = arr.length
    let res  = 0

    // 인접 행렬 만들기
    let distArr = initArr(n,arr)
    // 체크리스트 만들기
    let chList  = Array.from({length: n+1}, () => 0)

    // dfs 구현하기 
    chList[1] = 1
    DFS(1)

    return res
    
}

let arr=[[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]];
console.log(solution(5, arr));