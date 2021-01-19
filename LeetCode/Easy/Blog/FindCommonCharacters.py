# 2차원 배열
class Solution(object):
    def commonChars(self, A):
        
        """
        :type A: List[str]
        :rtype: List[str]
        """
        arr = [ [0] * 26 for _ in range(len(A)) ]
        res = []
        
        for i in range(len(A)) :
            for elem in A[i] :
                arr[i][ord(elem) - 97] += 1
        
        for i in range(97,123) :
            smallest = 2131320
            for j in range(len(A)):
                smallest = min(smallest, arr[j][i-97])
            while(smallest > 0):
                res.append(chr(i))
                smallest -= 1
        
        return res
            
# Counter library 사용
class Solution(object):
    def commonChars(self, A):
        
        """
        :type A: List[str]
        :rtype: List[str]
        """
        common = Counter(A[0])
        
        for i in range(1,len(A)) :
            for key in common.keys():
                common[key] = min(common[key], Counter(A[i])[key] )
        
        # elements() : 해당 key의 value만큼 key들의 목록을 얻을 수 있다 ( 즉, 0개인 key는 출력이 안된다)
        return sorted(common.elements())
            
               
        
        