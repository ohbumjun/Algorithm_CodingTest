class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        
        :type arr: List[int]
        :type k: int
        :rtype: int
        
        """
        
        def Kadane(nums):

            sumNums = [0] * ( len(nums) )
            sumNums[0] = nums[0]
            maxSum  = sumNums[0] 

            for i in range(1,len(nums)):
                sumNums[i] = max(nums[i], sumNums[i-1] + nums[i] )
                maxSum = max(sumNums[i], maxSum)


            return maxSum
        
        sumArr = sum(arr)
        MODULO = 10**9 + 7
        
        if k == 1 :
            return Kadane(arr)
        elif k == 0 or Kadane(arr) < 0 :
            return 0
        else:
            if sumArr > 0 :
                return  ( sumArr * (k-2)  + Kadane(arr * 2) )  % MODULO
            else : 
                return ( Kadane(arr * 2) ) % MODULO