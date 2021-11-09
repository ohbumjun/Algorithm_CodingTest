def fib2(n):
    first = 1
    second = 1 

    for i in range(2, n+1):
        temp = second
        second = first + second
        first = temp 
    
1 2
2 3
3 5