#rotating array by k positions(rotated right)
a = [ 13,4,5,56,65,23]
k=2
n=len(a)
k = k%n
a.reverse()      #whole array is reversed
a[:k] = reversed(a[:k])   # k number of elements are reversed
a[k:] = reversed(a[k:])   # all elements got reversed except k elements
