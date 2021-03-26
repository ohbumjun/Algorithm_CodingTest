const sum = (v) => v + ( v > 1 ? sum (v - 1) : 0 )

const sum = (v , prev = 0 ) => {
    prev += v
    return v > 1 ? sum( v - 1 , prev ) : prev  
}

// 삼항 연산자, &&, || 는 메모리에 잡지 않는다 

// prev는 함수 외적 메모리 
// prev는 loop 밖에 있는 메모리 
// 왜 loop 밖에 있는 메모리라고 하는거지 ?