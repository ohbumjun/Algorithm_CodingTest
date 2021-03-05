# https://leetcode.com/problems/lemonade-change/
# 860. Lemonade Change

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 거슬러 주는 것에 대한 문제, 거스름돈 단위를 생각한다
        five = ten = 0
        
        for bill in bills :
            # 5원이라면, 거스름돈 없이 5원을 추가하면 된다.
            if bill == 5:
                five += 1
            elif bill == 10 :
                if five == 0  :
                    return False
                five -= 1
                ten  += 1
            else :
                # 20원이라면
                # 1) 5, 10 원을 거슬러 줄 때
                if ten and five :
                    ten -= 1
                    five -=1
                # 2) 20 원을 거슬러 줄 때
                elif five >= 3 :
                    five -= 3
                else:
                    return False
            
        return True
        
        
        
        