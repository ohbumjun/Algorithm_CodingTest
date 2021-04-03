# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''

        > pivot을 설정한 이후

        > 3 부류로 나눈다
        1) pivot보다 큰 부류 : left >> 왜 큰 부류를 left로 분류하고, 배열 왼쪽에 둔다라는 개념을 취하는 것일까 ?? 문제는 kth largest elem을 물어보았다. 즉, 1번째,2번째로 큰 elem이 무엇이냐 !!
        따라서, 큰 값을 기준으로 왼쪽부터, 내림차순으로 내려가는 과정을 적용하는 것이다 
        2) pivot과 같은 부류   : mid
        3) pivot보다 큰 부류   : right

        > 각 배열의 len 구하기  
        left, mid만 구해도 된다 
        right 의 경우 , 전체 길이에서 ( left + mid )를 빼주면 되기 때문이다 


        > 범위에 따른 k 구하기

        자. len(left) , len(mid), len(right) 를 구했다고 해보자 
        각각의 길이를 S,M,L 이라고 한다면
        사실 우리는 '길이'를 바탕으로 '새롭게 정렬된' 배열을 만든 것처럼 생각할 수 있다

        즉, left 애들을 왼쪽, mid 애들을 가운데, right 애들을 오른쪽 

        이렇게 하는 이유는, 사실 우리는 'k번째'  element를 찾는 것이다
        이와 같이 '크기'를 기준으로 '정렬'된 형태의 array를 만든 것이라면 
        이제 left, mid, right 배열 각각의 '길이'와 'k'의 숫자를 비교하여
        'k번째 숫자'가 어떤 배열에 속하는지 판단할 수 있게 되는 것이다.

        mid 배열의 경우, 모든 숫자가 같다
        즉, k가 mid 에 포함된다면
        그냥 mid 값을 출력하면 된다

        반대로 말하면,
        k가 left 속하거나, right 속한다면
        해당 일부 배열에 대해서 재귀적으로 함수를 적용하여
        k가 mid 배열에 떨어질때까지
        반복하면 된다는 것이다 

        - 만일 k가 mid 범위안에 있다면
        mid 내 숫자 아무거나 출력해주면 된다 ( pivot과 같은 애들이기 때문에 )
        - 만일 left len 범위 안에 있다면, 거기에 대해서 다시 recursive
        - 만일 right len 범위 안에 있다면, 다시 recursive         


        '''
        pivot = random.choice(nums)

        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - (L+M))
        else:
            return mid[0]
