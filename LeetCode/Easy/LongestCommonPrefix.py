class Solution(object):
    def longestCommonPrefix(self, strs):
        
        """
        :type strs: List[str]
        :rtype: str
        """
        
        final_prefix = []
        
        if len(strs) == 0:
            return ""
    
        elif len(strs) == 1:
            return strs[0]
        
        # 최소 반복 횟수를 구하기 위해, 요소들의 최소 길이를 구한다
        min_len = min(map(len ,strs ))
        
        
            
        for idx in range(min_len):
            # 맨 처음 요소의 , 해당 idx 값을 가져온다
            Compare_value = strs[0][idx]

            for val in strs:
                if( val[idx] != Compare_value):
                    return ''.join([strSingle for strSingle in final_prefix])
            
            final_prefix.append(strs[0][idx])
        
        return ''.join([strSingle for strSingle in final_prefix])