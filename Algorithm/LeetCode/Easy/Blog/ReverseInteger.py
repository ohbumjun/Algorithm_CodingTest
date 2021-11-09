class Solution(object):
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if( x < 0 ): # 음수일 때
            x = -x
            IntList =  [int(num) for num in str(x) if str(x) != "0"][::-1]
            IntList =  "".join(map(str, IntList))
            if( int(IntList)  > pow(2,31)):
                return 0
            else:
                return -int(IntList)
        elif ( x == 0 ):
            return 0
        else: 
						# 양수일때 
						# 1) 문자열로 만들고 > split
						# 2) split한 애들을 뒤집기
						# 3) 뒤집은 애들 붙이기
						# 4) 붙인 애들 정수로 만들기
            IntList =  [int(num) for num in str(x) if str(x) != "0" ][::-1]
            IntList =  "".join(map(str, IntList))
            if( int(IntList) >  pow(2,31) - 1 ):
                return 0
            else:
                return int(IntList)
            return int(IntList)