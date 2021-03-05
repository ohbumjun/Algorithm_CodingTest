// https://exercism.io/my/solutions/6a464a1c52cc451b98ef6509a80fc294

const OPERATION = ['plus', 'minus', 'divided', 'multiplied' ]

export const answer = (phrase = "") => {
  
  // Throw an Error if phrase doesn't start like it should
  if(!phrase.startsWith("What is")){
    throw new Error("Unknown operation")
  }

  // Split phrase into an array with the numbers and operations
  // Don't forget ' ' after 'is'
  const parts = phrase.replace("What is ", "")
  .replace("?", "")
  .replace(/by /g, "")
  .split(" ")

  // Throw an Error if first elemetn isn't a number
  if(isNaN(parseInt(parts[0])))
    throw new Error("Syntax Error")

  let number = parseInt(parts[0])

  // Loop over each operation
  for(let i = 1 ; i < parts.length ; i += 2){
    // Throw an Error if the current element is a number
    if(parseInt(parts[i]))
      throw new Error('Syntax error')
    
    // Throw an error if the current element is not one of the basic 4 operations
    if(!OPERATION.includes(parts[i])){
      throw new Error("Unknown operation")
    }

    // Throw an error if there is no second number
    if(!parts[i+1] || isNaN(parseInt(parts[i+1])) )
      throw new Error("Syntax error")

    switch(parts[i]){
      case 'plus':
        number = number + parseInt(parts[i+1])
        break
      case 'minus':
        number = number - parseInt(parts[i+1])
        break
      case 'multiplied' :
        number = number * parseInt(parts[i+1])
        break
      case 'divided' :
        number = number / parseInt(parts[i+1])
        break

    }
  }
  return number
};
