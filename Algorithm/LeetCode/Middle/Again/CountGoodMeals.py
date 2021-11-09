class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        # dp + hash table
        # 1) 먼저, 현재 내가 접근하고 있는 값과, 배열 내 다른 원소의 합이 2 pow 형태인 애를 찾는 것 
        # 2) 이를 위해 각 숫자가 몇번 나왔는지 확인
        # 3) dp 개념으로, 앞에서부터, 현재 접근하고 있는 값이 배열의 마지막 원소일 때, good meal 개수
        # 왜 dp 개념으로 접근 ? Brute-Force 개념으로 접근하게 되면, pair를 중복하여 count 하게 될 수 있기 때문이다.

        total = 0
        mod   = 10 ** 9 + 7
        counts = collections.Counter() # 여기에 차례대로, 현재까지 접근한 원소, 그것의 개수.를 저장해간다 
        
        for x in deliciousness :
            for y in range(22): # 최대 2의 합은 2** 21 까지 될 수 있다
                target = ( 1 << y ) - x 
                if target in counts : 
                    total += counts[target]
            counts[x] += 1
        
        return total % mod
            
        
        
        
        