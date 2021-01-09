let fs = require('fs');
// var input = fs.readFileSync('/dev/stdin').toString().trim().split('\r\n');
let input = fs.readFileSync('js/test.txt').toString().trim().split('\r\n');
let NumOfMeeting = parseInt(input[0])
let Meetings = []
input.shift()


// 회의 정보 입력받기
for(let i = 0 ; i < NumOfMeeting ; i++){
    input[i] = input[i].split(' ')
    Meetings.push([parseInt(input[i][0]), parseInt(input[i][1])])
}

Meetings.sort((a,b) => {
    return a[1] - b[1]
})

let start = 0 
let end   = 0
let FinalNum = 0 

Meetings.forEach((meeting) => {
    if( meeting[0] >= end){
        end = meeting[1]
        FinalNum += 1
    }
})

console.log(FinalNum)