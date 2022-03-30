def solution(piles):
    total = 0
    l = sorted(piles,reverse = True)
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            total += i + 1
    return total

data = [5,2,1,6]

print(solution(data))