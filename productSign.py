def _arraySign(nums):
    product = 1
    for number in nums:
        product *= number
        
    if product > 0:
        return 1
    elif product < 0:
        return -1
    else:
        return 0

def arraySign(nums):
    negatives = 0
    for number in nums:
        if number == 0:
            return 0 
    
        if number < 0:
            negatives += 1
    
    if negatives%2 != 0:
        return -1
    else:
        return 1

nums = [1,5,0,2,-3]

arraySign(nums)