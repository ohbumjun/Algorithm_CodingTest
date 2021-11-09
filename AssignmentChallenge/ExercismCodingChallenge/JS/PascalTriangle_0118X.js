

// https://exercism.io/my/solutions/7072833272e045f7b5113b87c13b9b73

//
// This is only a SKELETON file for the 'Pascals Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//


export const rows = (num) => {

    const rowCombinations = (num) => {
      if( num == 1 ){
        return 1
      }else{
        
        let sum = 1
        
        for(let i = 1 ; i <= num - 1 ; i++ ){
          sum += eachCombination( num - 1, i )
        }
  
        return sum
      }
    }
  
    const eachCombination = (n,m) => {
      let up = 1
      let down = 1
      for(let i = n; i > n - m ; i--){
        up *= i
      }
      for(let i = 1; i <= m ; i++){
        down *= i
      }
      return up / down
    }
  
    let totalSum = 0
  
    if(num == 0){
      return []
    }
  
    for(let i = 1; i <= num; i++){
      totalSum += rowCombinations(i)
    }
  
    return totalSum
  
  }