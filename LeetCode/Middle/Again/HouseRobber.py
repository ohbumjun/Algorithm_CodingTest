# https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dy = [0,0,0]
        for i in range(3, len(nums) + 3) :
            dy.append(max(dy[i-2] , dy[i-3]) + nums[i-3])
            
        
        return max(dy)
        