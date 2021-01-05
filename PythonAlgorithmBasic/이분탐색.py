def binsearch(n, S, x) :
    low = 1
    high = n
    location = 0 
    while( low <= high and location == 0 ):
        mid = (low + high) // 2