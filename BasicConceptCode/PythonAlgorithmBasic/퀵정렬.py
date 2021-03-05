def partition2( S, low, high):
    pivotitem = S[low]
    i = low + 1;
    j = high'
    while( i <= j):
        while(S[i] < pivotitem ):
            i +=1 
        while( S[j] > pivotitem ):
            j -= 1
        if( i < j ):
            S[i], S[j] = S[j], S[i] # swap
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low] # swap
    return pivotpoint

    def quicksort( S, low, high):
        if( high > low) :
        pivotpoint = partition2(S, low, high)
        quicksort2(S, low, pivotpoint -1)
        quicksort2(S, pivotpoint+1, high)

