class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        # 배열 설정
        tripRoute = [0] * 1001
        
        # trips 돌면서, st, ed 범위에 인원 추가
        for trip in trips :
            
            st = trip[1]
            ed = trip[2]
            
            for i in range(st,ed) :
                tripRoute[i] += trip[0]
            

        for x in tripRoute :
            if x > capacity :
                return False
       
        
        return True