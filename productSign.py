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