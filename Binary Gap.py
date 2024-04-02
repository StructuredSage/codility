# Binary Gap: To find the max amount ot consecutive zeroes

def solution(N):
    N=bin(N)[2:]
    b=0
    maxb=0
    for i in N:
        if int(i)==0:
            b+=1
        elif int(i)==1:
            maxb = max(b,maxb)
            b=0
    return maxb

N=2578
print(f"Number: {N} | Binary: {bin(N)[2:]} | Solution: {solution(N)}")