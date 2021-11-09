import sys
from collections import deque
sys.stdin = open("input.txt", "rt") # input 내용을 파일에서 가져온다 

# 중복 조합
def DFS(L, val):

    if L == m :
        for x in res :
            print( x , end = ' ' )
        print()
    else:
        # n 이 아니라 len(arr) 이라는 것이 중요. 우리는 중복을 제거한 배열에 대해 적용하는 것이므로
        # 또한 중복 조합이므로, 별도의 check list 배열이 필요 없
        for i in range(val,len(arr)):
            # 값 넣기
            res[L] = arr[i]
            # DFS
            DFS( L + 1, i)
            
            
    


if __name__ == "__main__" :

    n , m = map(int,input().split())
    '''
    여기서 set을 통해 중복값을 제거하는 것이 중요하다.
    무슨 말일까 ?

    < 중복 조합 >
    조합을 만들어내되, 중복해서 선택 가능한 것

    4 4 2 에 대해 중복 조합을 만든다고 할 때 ,

    사실상 4 2 를 이용해서 중복 조합을 만든다는 것과 같다.

    예를 들어 4 4 2 를 이용해서
    4 2 라는 조합을 만들어낼 때

    앞의 4를 이용하던
    뒤에 4를 이용하던
    결과는 같다.

    그러나, 2개의 경우를 다르게 생각하면 안된다

    그래서 애초부터 모든 중복을 제거하고 시작하는 것이다
     
    '''
    arr   = sorted(set(list(map(int,input().split()))))
    res   = [0] * m
    ch    = [0] * n
    AllArr = set()

    DFS(0,0)



                

    

    
