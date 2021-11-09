/*

접근방법
1) Permutation 수열을 만들고
2) 최댓값을 찾는다 

function solution(numbers,  set = [], answers = []) {
    
    
    if( !numbers.length){
            // 더이상 다룰 수 있는 수가 없다면 
            answers.push([...set].join(''))
        }

        for(let i = 0 ; i < numbers.length ; i++){
            // remove current num from nums array
            const newNums = numbers.filter((n, index) => index !== i )
            // add current num we chose
            set.push(numbers[i])
            solution(newNums, set, answers)
            set.pop() 
            // 재귀 과정에서 set 에 push된 애를 제거해준다 ( 단계적으로 진행되                 어서, 한번 pop이 이루어지는 것이 아니라
            // 다수의 숫자가 없어질 수 있다 )
        }
    
    let maxValue = 0
    answers.forEach((answer) => {
        answer = answer.join('')
        if( answer > maxValue )
            maxValue = answer
    })
    
    return String(maxValue)
}


< 결과 > : 	실패 (signal: aborted (core dumped))
*/


/* 두 수 a, b를 붙였을 때, 더 큰 수를 기준으로 정렬하면 되겠다라는 생각이 들었고, 몇 가지 사례를 통해 확인해보니 이 생각에 확신이 들었다. */
function solution(numbers) {
    
    var answer = numbers.map(c=> c + '').
    				sort((a,b) => (b+a) - (a+b)).join('');
    
    // 1. numbers.map(c => c + '') : 각 숫자들을 문자로 변환
    // 2. sort((a,b) => (b+a) - (a+b)) : 문자로 변환된 숫자를 연결하여, 더 큰수를 기준으로 비교 정렬
    // ex. ('3', '30') => ('303') - ('330')
    // 3. join('') : 문자열 합치기 

    return answer[0]==='0'? '0' : answer;
    // 4. 배열이 -으로만 구성되었을 경우, '0'만 출력, 그렇지 않다면, 맨 앞은 가장 큰수이므로, 가장 큰수 출력
}