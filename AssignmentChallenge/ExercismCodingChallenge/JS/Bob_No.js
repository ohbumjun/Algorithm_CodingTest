// https://exercism.io/my/solutions/8661683df15345a386f088acdff1790a

export const hey = (message) => {
    // 1. 일반 질문 : "?"             : Sure.
    // 2. 마지막 "?" 이되 모두 대문자  : Calm down, I know what I'm doing!
    // 3. 모두 대문자                  : Whoa, chill out!
    // 4. 아무것도 말 안함             : Fine. Be that way!
    // 5. 그외                        : Whatever
    const lastStr = message.slice(message.length - 1)
    const isAllCapital = message == message.toUpperCase()
  
    if( isAllCapital == false && lastStr == '?' ){
      return "Sure."
    }else if( isAllCapital == true && lastStr == '?'   ){
      return "Calm down, I know what I'm doing!"
    }else if( isAllCapital == true ){
      return "Whoa, chill out!"
    }else if( message == ""){
      return "Fine. Be that way!"
    }else{
      return "Whatever."
    }
  };