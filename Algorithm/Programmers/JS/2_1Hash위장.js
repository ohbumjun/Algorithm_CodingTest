function solution(clothes) {
    
    let answer = 1;
    
    // 각 의상에 따른 갯수를 저장하는 Object
    let ClothObject = {}
    
    clothes.forEach((cloth) => {
        if(ClothObject[cloth[1]] == undefined)
            ClothObject[cloth[1]] = 1
        else
            ClothObject[cloth[1]] += 1
    })
    
    // ex. 얼굴 종류에 해당하는 의상이 3개라면, 안입는 경우의 수도 존재하므로, + 1을 해주어야 한다
    // 단, 안입는 경우의 수는 제외해야 하므로, 마지막 값에서 -1을 해주어야 한다
    for( let i in ClothObject){
        answer *= ( ClothObject[i] + 1 )
        
    }
    
    return answer -1 
    
    
}