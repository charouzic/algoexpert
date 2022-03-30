def solution(A, B, C, D):
    # write your code in Python 3.6

    if A == B and B == C and C == D:
        return 0

    first = (A-B)**2 + (C-D)**2
    second = (A-C)**2 + (B-D)**2
    third = (A-D)**2 + (B-C)**2

    return max(first, second, third)

print(solution(1,-1,-1,1))

print(solution(1,2,3,4))

print(solution(10,10,10,10))