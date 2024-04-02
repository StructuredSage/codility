#Cyclic Array: to displace each element of an array K amount of positions

def solution (K, A):
    L = len(A)
    N = [None] * L
    for i in range(0,L):
        N[(i+K)%L] = A[i]
    return N

K = 1
A = [1,2,3]
print (f"New Array: {solution(K,A)}")