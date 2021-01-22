# https://codeforces.com/problemset/problem/1335/B
'''
so we are making 
'n' length array

and , inside the 'n' length array, 
'a' length , sub array exist,

also, inside the 'a' length subarray, 
'b' distinct alphabet should exist

SO !! we go backwards,  
we make 'a'length subarray, by using 'b' distinct alphabets

and we make 'n' length array, by using 'a' length subarray 

ex.
n   a   b
7   5   3

we make 'b' distinct alphabet
"abc"

amon 'a' length places, we can put 3 distinct element

a b c a b 
_ _ _ _ _

now by 'a' length subarray, we make 'n' length array

a b c a b a b 
_ _ _ _ _ _ _


'''

def makeString( n, a, b ) :
    
    # final answer arr
    res = []
    # fill the substring 'a', by 'b' distinct element
    arr = []
    A   = a

    while a > 0:
        for i in range(97 , 97 + b  ) :
            arr.append(chr(i))
        a = a - b

    a = A
    arr = arr[:a]

    sN = n
    # make 'n' length array from 'a' length sub array
    while n > 0 :
        for i in range(len(arr)) :
            res.append(arr[i])
        n -= a

    return res[:sN]
        


N = int(input())

for _ in range(N):
    n,a,b = map(int, input().split())
    print( ''.join( makeString(n,a,b ) ) )

