# Odd Occurences in Array: Return the number that doesn't have an equal counterparty

# create a dictionary, track count of elements and then return the odd one
def solution1 (A):
    counts = {}
    for num in A:
        counts[num] = counts.get(num, 0) + 1
    
    for num, count in counts.items():
        if count % 2 != 0:
            return num

# sort elements, add extra element to prevent index out of range, jump by 2 positions and compare next item. If different return
def solution2 (A):
    A.sort()
    A.append(-1)
    for i in range(0, len(A), 2):
        if A[i] != A[i+1]:
            return A[i]

A = [9,3,9,3,9,7,9]

print(solution1(A))
print(solution2(A))