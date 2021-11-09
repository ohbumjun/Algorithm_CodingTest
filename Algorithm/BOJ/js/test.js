
function solve(){
    var fs = require('fs');
    
    // var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
    var input = fs.readFileSync('test.txt').toString().trim().split('\n');
    
    // 수열에 들어갈 수 있는 숫자의 종류
    var n = parseInt(input[0].split(' ')[0])
    var m = parseInt(input[0].split(' ')[1])

    var res = new Array(m ).fill(0)
    var ch  = new Array(n + 1).fill(0)

    var result = ' '

    dfs(1)

    console.log(result.trim())

    function dfs(L){
        if( L == m + 1 ){
            result += `${res.join(' ')}\n`
        }
        else{
            for(let i = 1 ; i <= n ; i++){
                if( ch[i] == 0 ){
                    res[L-1] = i
                    // 방문 처리
                    ch[i] = 1
                    // 다시 dfs
                    dfs(L+1)
                    // 방문 처리 해제
                    ch[i] = 0
                } 
            }
        }
    }
}



solve()