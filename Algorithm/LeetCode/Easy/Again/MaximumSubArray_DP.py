class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = nums[0]
        global_max = nums[0]
        
        for x in range(1,len(nums)) :
            # local
            local_max = max(local_max + nums[x] , nums[x])
            global_max = max(local_max, global_max)
        
        
        return global_max