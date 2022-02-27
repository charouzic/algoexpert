array = [-3, -2, -1]

res = []
res.append(array[0]**2) 

for i in range(1, len(array)):
    
    square = array[i]**2
    res.append(square)
    
    if res[i] < res[i-1]:
        res[i], res[i-1] = res[i-1], res[i] 