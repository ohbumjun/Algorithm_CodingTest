function solve(){
    var fs = require('fs');
    
    // var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
    var input = fs.readFileSync('js/test.txt').toString().trim().split('\r\n');
    var board = []
    var minPzLenTotal = 1219999
    let hs = []
    let pz = []
    let pzNum = 0 
    

    // 테스트 케이스 갯수 정보 받아들이기 
    var n = parseInt(input[0].split(' ').shift())
    var m = parseInt(input[0].split(' ').shift())
    console.log("m", m)
    let pzCases = new Array(m).fill([])

    input.shift() // n,m 정보 삭제 

    // 집, 피자집 정보 생성
    for(let i = 0 ; i < input.length ; i++){
        board.push(input[i].split(' ').map(num => parseInt(num)))
    }

    // 집, 피자 각각 따로 배열로 정리
    for(let i = 0 ; i < n; i++){
        for(let j = 0 ; j < n; j++){
            if( board[i][j] == 1 ){
                hs.push([i,j])
            }else if(board[i][j] == 2){
                pz.push([i,j])
            }
        }
    }

    pzNum = pz.length
    console.log(pz)
    dfs( 0 , 0 )

    console.log(minPzLenTotal)

    function dfs(L, val){
        if(L == m){
            // 하나의 pzCases 배열이 만들어진다.
            var minPzLenPerCase = 0
            // 한개의 조합 완성
            for(let i = 0 ; i < hs.length; i++){

                nowHs = hs[i]
                hsX = nowHs[0]
                hsY = nowHs[1]
                minLenPerHouse = 129999239
                
                for(let j = 0 ; j < pzCases.length; j++){
                    pzX = pzCases[j][0]
                    pzY = pzCases[j][1]
                    minLenPerHouse = minLenPerHouse < ( Math.abs(pzX - hsX) + Math.abs(pzY - hsY) ) ?  minLenPerHouse : ( Math.abs(pzX - hsX) + Math.abs(pzY - hsY) )
                }
                minPzLenPerCase += minLenPerHouse
            }
            minPzLenTotal = minPzLenTotal < minPzLenPerCase ? minPzLenTotal : minPzLenPerCase 
            console.log("minPzLenTotal", minPzLenTotal)
            return

        }else{
            for(let i = val ; i < pzNum; i++){
                pzCases[L] = pz[i]
                dfs(L + 1, i + 1) 
            }
        }
    }
}



solve()