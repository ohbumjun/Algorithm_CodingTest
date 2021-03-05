// https://www.acmicpc.net/problem/10828
function solve(){
    var fs = require('fs');
    
    // var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
    var input = fs.readFileSync('js/test.txt').toString().trim().split('\r\n');
    var stack = []
    var numOfRepeat = parseInt(input[0])
    input.shift()

    for(let i = 0 ; i <  numOfRepeat ; i++){
        input[i] = input[i].split(' ')
        Command = input[i][0]
        if(Command == "push"){
            stack.push(parseInt(input[i][1]))
        }else if(Command == "top"){ 
            if(stack.length == 0){
                console.log(-1)
            }else{
                console.log(stack[stack.length-1])
            }
        }else if(Command == "size"){
            console.log(stack.length)
        }else if(Command == "empty"){
            let IsEmpty = ( stack.length == 0 ) ? 1 : 0
            console.log(IsEmpty)
        }else if(Command == "pop"){
            if(stack.length == 0){
                console.log(-1)
            }else{
                console.log(stack.pop() )
            }
        }
    }
}



solve()