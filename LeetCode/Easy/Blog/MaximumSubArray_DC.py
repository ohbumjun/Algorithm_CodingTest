# https://leetcode.com/problems/maximum-subarray/submissions/

# Divide And Conquer
class Solution(object):
    def maxSubArray(self, nums):

        def divideAndConquer(low, high):
            if low == high : 
                return nums[low]

            m = ( low + high ) // 2
            left  = divideAndConquer( low , m )
            right = divideAndConquer( m+1 , high )

            leftMid = leftMidMax  = nums[m]
            
            for i in range( m-1 , low -1, -1 ) :   
                leftMid += nums[i]
                leftMidMax = max( leftMid , leftMidMax)

            rightMid = rightMidMax = nums[m+1]
            for i in range(m+2, high + 1):
                rightMid += nums[i]
                rightMidMax = max( rightMid , rightMidMax )

            return max( left, right, leftMidMax + rightMidMax)
    
        return divideAndConquer( 0, len(nums) -1)
            
           
       