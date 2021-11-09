import sys
from collections import deque
# sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

if __name__ == "__main__" :
    
    calculation = input()

    divided = calculation.split('-')
    result = 0
    
    # 마이너스를 만나기전, 맨 처음 값 더한다
    for x in divided[0].split('+'):
        result += int(x)
        

    # 이후에는, - 를 기준으로 묶어서, 계속 빼준다.
    for bunch in divided[1:]:
        for j in bunch.split('+'):
            result -= int(j)

    print(result)
    
        
            
            
            
                
            
    
