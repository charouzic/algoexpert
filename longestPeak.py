array = [1, 1, 3, 2, 1]

arrLen = len(array)
peakLen = 0



for i in range(1, arrLen-1):
    right = i+1
    left = i-1
    currPeakCount = 1
    
    if array[left] < array[i] and array[right] < array[i]:
        #isTip = True
        previous = i
        while left >= 0 and array[left] < array[previous]:
            currPeakCount += 1
            left -= 1
            previous -= 1
            
        future = i
        while right < arrLen and array[right] < array[future]:
            currPeakCount += 1
            right += 1
            future += 1
        
        if peakLen < currPeakCount:
            peakLen = currPeakCount

print(peakLen)