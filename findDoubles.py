def findDoubles(numbers):

    numbers = sorted(numbers, reverse=True)
    d = {}
    res = []
    # number: occurence, product

    for number in numbers:
        if number in d:
            d[number][0] += 1 
        else:
            d[number] = [1, 2*number]

    for i in d.keys():
        doubleValue = d[i][1]
        if doubleValue in d and d[doubleValue][0] == 1:
            res.append(i)
            
    res.sort()
    return res

numbers = [1,2,3,4,5,6,7,8,9,0,8]

numbers2 = [2,9,10,6]

numbers3 = [1,1,2]

print(findDoubles(numbers3))