def maximumUnits(boxTypes, truckSize):
        # sort the list by the numberOfUnitsPerBoxi
        res = 0
        #sorted(data, key=lambda tup: tup[1], reverse=True)
        sortedBoxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        for i in range(len(sortedBoxTypes)):
            
                noBoxes = sortedBoxTypes[i][0]
                
                dif = truckSize - noBoxes
                if  dif >= 0:
                    res += noBoxes*sortedBoxTypes[i][1]
                    truckSize -= noBoxes
                else:
                    res += truckSize*sortedBoxTypes[i][1]
                    break
                
        return res

data = [[1,3],[2,2],[3,1]]
truckSize = 4

print(maximumUnits(data, truckSize))