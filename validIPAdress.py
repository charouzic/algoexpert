def validIPAddresses(string):
    # Write your code here.
    ipPart = ""
    res = []
    
    for first in range(1, min(len(string), 4)):
                       
        ipAddressParts = ["", "", "", ""]
            
        ipAddressParts[0] = string[:first]
        
        if not isValidPart(ipAddressParts[0]):
            continue
            
        for second in range(first + 1, first + min(len(string) - first, 4)):
            ipAddressParts[1] = string[first:second]
        
            if not isValidPart(ipAddressParts[1]):
                continue
            
            for third in range(second + 1, second + min(len(string) - second, 4)):
                ipAddressParts[2] = string[second:third]
                ipAddressParts[3] = string[third:]

                if isValidPart(ipAddressParts[2]) and isValidPart(ipAddressParts[3]):
                    res.append('.'.join(ipAddressParts))
                    
    return res
                               
                

def isValidPart(number):
    intNumber = int(number)
    if intNumber > 255:
        return False
    
    return len(str(intNumber)) == len(str(number))


## COMPLEXITY
# time --> O(1)
# space --> O(1)
# it's because there's up to 12 digit numbers and we can create only given number of IP addresses therefore 
# the running time is not dependent on the input