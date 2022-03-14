def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return traverse(height, maxSteps, 0)

# at each stair I will iterate through the numbers ranging from 1 to maxSteps and call the function recursively

def traverse(height, maxSteps, ways):
    if height < 0:
        return 0
    
    elif height == 0:
        return 1
        
    else:
        for noSteps in range(1, maxSteps + 1):
            ways += traverse(height-noSteps, maxSteps, 0)
            
    return ways

## COMPLEXITY
# time -> O(s^h) where h is the height of the staircase and s is the maximum steps we can take
# space: O(h)

## MEMOIZATION
def _staircaseTraversal(height, maxSteps):
    # Write your code here.
    memotable = {0:1, 1:1}
        
    return _traverse(height, maxSteps, 0, memotable)

# at each stair I will iterate through the numbers ranging from 1 to maxSteps and call the function recursively

# use memoization to keep track of the heights and ways to get from that height to the top of the stair

def _traverse(height, maxSteps, ways, memotable):
    if height in memotable:
        return memotable[height]
        
    else:
        for noSteps in range(1, min(maxSteps, height) + 1):
            ways += traverse(height - noSteps, maxSteps, 0, memotable)
                
        memotable[height] = ways
                
    return ways

## COMPLEXITY
# time -> O(s*h) where h is the height of the staircase and s is the maximum steps we can take
# space: O(h)

## DYNAMIC PROGRAMMING
def __staircaseTraversal(height, maxSteps):
    # Write your code here.
    
    # using dynamic programming
    
    numberOfWays = [0 for _ in range(height+1)]
    
    numberOfWays[0] = 1
    numberOfWays[1] = 1
    
    for currHeight in range(2, height+1):
        step = 1
        while step <= currHeight and step <= maxSteps:
            numberOfWays[currHeight] = numberOfWays[currHeight] + numberOfWays[currHeight-step]
            step += 1
        
    return numberOfWays[-1]

