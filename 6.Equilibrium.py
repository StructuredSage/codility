def solution(A):
    if len(A)<2:
        return 0
    s = sum(A)

    minDiff = 2000
    sL = 0
    for i in range (0,len(A)-1):
        sL+=A[i]
        diff=abs(2*sL-s)
        minDiff = min(minDiff, diff)
    
    return minDiff