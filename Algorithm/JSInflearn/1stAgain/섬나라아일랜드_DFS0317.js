function solution(arr){
    // 답
    let answer = 0
    let len = arr.length

    // 상,하,좌,우 , 왼위대, 오위대, 왼아대, 오아대 
    let dCol = [0,0,-1,1, -1, 1, -1, 1]
    let dRow = [-1,1,0,0, -1,-1,  1,,1]

    const isValid = (num) => { 
        let valid = ( 0 <= num && num < len ) ? true : false
        return valid   
    }

    const DFS = (row,col) => {
        arr[row][col] = 0
        for(let i = 0 ; i < 8; i++){
            let nCol = col + dCol[i]
            let nRow = row + dRow[i]
            if(isValid(nCol) && isValid(nRow) && arr[nRow][nCol] == 1){
                DFS(nRow,nCol)
            }
        }
    }

    for(let i = 0 ; i < len; i++ ){
        for(let j = 0 ; j < len ; j++){
            if(arr[i][j] == 1){
                answer += 1
                DFS(i,j)
            } 
        }
    }

    return answer
}

let arr=[[1, 1, 0, 0, 0, 1, 0], 
        [0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 0]];

console.log(solution(arr));