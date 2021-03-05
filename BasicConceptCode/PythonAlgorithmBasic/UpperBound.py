
'''
Upper Bound 란
원하는 k 값을 초과한 값이 처음 나오는 위치를 찾는 과정

즉, 원하는 k 값보다 큰 값을 찾아야 하는 것이다 

'''
def upper_bound(start, end ,num) :
    while start < end :
        mid = ( start + end ) // 2
        if res[mid] == num: # res[mid] 가 num과 같다면, 그 값을 포함시킬 필요가 없다. num보다 큰 값을 찾는 것이므로
            start = mid + 1
        elif res[mid] < num :
            start = mid + 1
        elif res[mid] > num : # 우선 해당 mid 값을 후보에 두되, 더 작은 값이 나타날 수도 있으니 계속 진행
            end = mid
    
    # 결국 start == end 일때 break 하게 된다
    return end
