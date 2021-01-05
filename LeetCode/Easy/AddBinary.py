class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        # 각 문자열을 이진수로 변환
        bin_a = int(a,2) 
        bin_b = int(b,2)
        
        # 10진수를 2진수로 변환 : 0이 될때까지 나누고, 나머지를 역순 정렬
        decimal = bin_a + bin_b
        binArray = list()
        idx = 0
        
        while(1):
            binArray.append(decimal % 2)
            decimal = decimal // 2
            if(decimal == 0):
                break;
            
        return  ''.join( str(i) for i in  binArray[::-1] )