const solution = (num,res) => {
    if(num > 1){
        res.push(num % 2 ) 
        num = parseInt(num / 2)
        return solution(num,res)
    }else{
        res.push(num)
        res = res.reverse().join('')
        return res
    }
}