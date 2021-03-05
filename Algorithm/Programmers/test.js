var a = "0000000000"
a = a.split('')
console.log( "a.length",  a.length)

var result = []

for(let i = 0 ; i < a.length; ){
    result.push(a.slice(i, i+2).join(''))
    i+= 2 
}

console.log("result", result )

result.splice(0,0, "99" )

console.log(result)