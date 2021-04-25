const solution = (arr) => {
    /*
        dp[i] : i번째 원소가 증가부분 수열의 가장 마지막에 왔을 때의
        최대 증가수열 길이

        1) arr[i]가 arr[i-1]보다 크다면
            그냥 뒤에 붙여주면 되기 때문에
            dp[i] = dp[i-1] + 1

        2) 같다면, 그냥 dp[i] = dp[i-1] 

        3) arr[i]가 arr[i-1] 보다 작다면,
            arr[i]보다 작으면서 arr[i-1] 앞에 있는 숫자중에서
            최대의 dp[i] 를 갖는 dp[i] + 1
            만약, 이것에 해당하는 숫자가 하나도 존재하지 않는다면 
            그저 1 로 할당한다 
    */
   const len = arr.length
   let ans = -1
   let dp = Array(len).fill(0)
   dp[0]  = 1

   // 사실 한가지로 정리할 수 있다
   // 자기보다 앞의 칸을 탐색하면서
   // 자기보다 작으면서(arr[i]) , dp는 그중에서 최고인 요소를 찾고,
   // 거기에 +1, 만약 그러한 요소가 없다면, 1을 대입 
   
   return ans
}

const arr = [5,3,7,8,6,2,9,4]
// const arr = [2,7,5,8,6,4,7,12,3]
console.log(solution(arr))

/*
순서만 유지하면서 뽑아내야 한다 



*/