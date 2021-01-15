class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash = { }
        hash[1] = 1
        hash[2] = 2
        
        
        if( n >= 3):
            for i in range(3, n+1):
                hash[i] = hash[i-1] + hash[i-2]
                
        return hash[n]