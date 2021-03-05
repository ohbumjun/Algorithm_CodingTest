def mergesort(S):
    n = len(S)
    if ( n <= 1):
        return S
    
    else :
        mid = n // 2
        U = mergesort(S[0 : mid])
        V = mergesort(S[mid:n])
        return merge(U,V)