class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # 초기값을 먼저 설정한다 
        start_n = 1
        result  = '1' #result가 바로, 앞으로 계속 바뀔 문자열
        
        while start_n < n :    # n까지 반복한다 
            cur_n = result[0]  # 현재값 가져오고
            cnt   = 1          # 카운트는 1로 해준다
            new_result = ""    # 새로운 바뀐 문자열(temp 개념)
            
            if( len(result) == 1 ): # 맨첫번째 케이스( "1" )에 해당한다면,  
                start_n += 1
                result  = '11'
                continue
                
            for i in range(1, len(result)): # 본격적으로 다시 시작 
                if cur_n != result[i]: # 다른 값이 나타나면 
                    new_result += str(cnt)
                    new_result += str(cur_n)
                    
                    # reset
                    cur_n = result[i]
                    cnt   = 1
                else :
                    cnt  += 1
                
                # last idx
                if len(result) -1 == i :
                    new_result += str(cnt)
                    new_result += str(cur_n)
            start_n +=1
            result = new_result
         
        return result