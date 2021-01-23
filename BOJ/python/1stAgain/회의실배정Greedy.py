import sys
from collections import deque
sys.setrecursionlimit(10000)

if __name__ == "__main__" :
    
    n = int(input())
    meeting = []
    
    for i in range(n):
        s, e = map(int,input().split())
        meeting.append((s,e))

    # end 시간 기준 정렬
    meeting.sort(key = lambda x : (x[1], x[0]))

    start = 0
    end   = 0
    res   = 0
    
    for st, ed in meeting :
        if st >= end :
            res += 1
            end   = ed
    print(res)
            
            
            
                
            
    
