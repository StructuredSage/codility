# Perm Missing Elem: To find the missing element in an array

def solution(A):
    if(len(A) == 0):
        return 1
    A.sort()

    for i in range(0, len(A)):
        if A[i] != i+1:
            return i+1
    return (len(A) + 1)

A = [7,5,1,3,2,4]
print(solution(A))