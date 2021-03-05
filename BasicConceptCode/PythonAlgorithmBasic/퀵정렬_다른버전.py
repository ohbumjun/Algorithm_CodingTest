def quicksort( S, low, high):
    if( high > low) :
        pivotpoint = partition(S, low, high)
        quicksort(S, low, pivotpoint -1)
        quicksort(S, pivotpoint+1, high)


def partition( S, low, high):
    pivotitem = S[low]
    j = low
    for i in range(low+1, high+1):
        if(S[i] < pivotitem):
            j += 1;
            S[i],S[j] = S[j],S[i] # swap
    pivotpoint = j
    S[low],S[pivotpoint] = S[pivotpoint], S[low] #swap
    return pivotpoint




