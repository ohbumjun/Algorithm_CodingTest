# Python
def differenece(a,b):
    _b = set(b)
    return [ item for item in a if item not in _b] # a 중에서 b에 있지 않은 것들

# examples : a 배열중에서, b 와 다른 값
differenece([1,2,3], [1,2,4]) # [3]