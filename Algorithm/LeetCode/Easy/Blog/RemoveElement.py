class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
				# list comprehension을 통해, nums 원소 중에서 val이 아닌 원소들만 뽑아 temp 에 넣기
        temp = [ item for item in nums if item != val]
        
				# temp 요소들을 nums에 넣기
        for i in range(len(temp)):
            nums[i] = temp[i]
        
				# temp 길이 만큼의 원소들만 앞에서부터 남기기
        nums = nums[:len(temp)]
            
        return len(temp)