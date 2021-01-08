// https://bitwise.tistory.com/70

dx = [-1,0,1,0]
dy = [0,1,0,-1]

function solve(){
    var fs = require('fs');
    // var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
    var input = fs.readFileSync('js/test.txt').toString().trim().split('\n');
    // 테스트 케이스 갯수 정보 받아들이기 
    var t = parseInt(input[0])
    input.shift() // 테스트케이스 갯수 정보 삭제 
    var count = 0 
    var i = 1
    var answer = []
    let cabbageLocation

    while( t != count){

        var testCaseInfo = input[i-1].split(' ')
        var numOfCol = parseInt(testCaseInfo[0]) // 가로 길이 
        var numOfRow = parseInt(testCaseInfo[1]) // 세로 길이 
        var k = parseInt(testCaseInfo[2]) // 배추가 심어진 위치의 갯수
        var eachCnt = 0

        // arr[n][m]
        cabbageLocation = Array.from(Array(numOfRow), () => Array(numOfCol).fill(0))
        for(var c = i; c< k + i; c++){
            var temp = input[c].split(' ').map((element)=> element/1)
            var col = temp[0]
            var row = temp[1]
            cabbageLocation[row][col] = 1
        }
        
        // 배추 dfs
        for(let i = 0 ; i < numOfRow ; i++){
            for(let j = 0 ; j < numOfCol ; j++){
                if(cabbageLocation[i][j] == 1){
                    // 방문 처리
                    cabbageLocation[i][j] = 0
                    dfs(i,j)
                    eachCnt++
                }
            }
        }
        console.log(eachCnt)
        i += k + 1 // 다음 테스트 케이스를 위해 인텍스 조정
        count ++
    }

    function dfs(nowX,nowY){
    
        for(let k = 0 ; k < 4 ; k++){
            newX = nowX + dx[k]
            newY = nowY + dy[k]
            if( ( 0 <= newX && newX < numOfRow)  && ( 0 <= newY && newY  < numOfCol ) ){
                if(cabbageLocation[newX][newY] == 1){
                    // 방문 처리
                    cabbageLocation[newX][newY] = 0
                    // dfs
                    dfs(newX, newY)
                }
            }
        }
    }

}



solve()