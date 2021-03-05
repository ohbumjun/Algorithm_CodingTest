var permute = function(nums, set = [], answers = [] ){
    // 그림상으로 보면, nums는 파란색의 왼쪽 배열
    // set은 오른쪽 배열
    if( !nums.length){
        // 더이상 다룰 수 있는 수가 없다면 
        answers.push([...set])
    }

    for(let i = 0 ; i < nums.length ; i++){

        // remove current num from nums array
        const newNums = nums.filter((n, index) => index !== i )
        
        // add current num we chose
        set.push(nums[i])

        permute(newNums, set, answers)

        set.pop() 
        // 재귀 과정에서 set 에 push된 애를 제거해준다 ( 단계적으로 진행되어서, 한번 pop이 이루어지는 것이 아니라
        // 다수의 숫자가 없어질 수 있다 )

    }
}