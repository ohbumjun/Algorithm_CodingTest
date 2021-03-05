var arrLen = readline()
var arr = readline().split(" ").map(x => parseInt(x)).sort();
// count how many each number exist
var arrCnt = new Array(100001).fill(0)
// dy[j] == max sum if J is chosen among Input 
var dy = new Array(100001).fill(0)

// count how many elem
arr.forEach(value => arrCnt[value] += 1)

dy[0] = 0
dy[1] = arrCnt[1]

var i = 2
while( i < 100001){
    dy[i] = Math.max(dy[i-1] , dy[i - 2] + i * arrCnt[i]  );
    i++
}

print(dy[dy.length - 1])