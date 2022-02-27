array = [5, 1, 4, 2]
res =[] 
arrLen = len(array)

leftProducts = [1 for _ in range(arrLen)]
rightProducts = [1 for _ in range(arrLen)]

for i in range(1, arrLen):
    leftProducts[i] = array[i-1] * leftProducts[i-1]
    
for j in reversed(range(arrLen-1)):
    rightProducts[j] = array[j+1] * rightProducts[j+1]
    
for k in range(arrLen):
    res.append(leftProducts[k] * rightProducts[k])