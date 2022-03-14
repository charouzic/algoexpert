def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return traverse(height, maxSteps, 0)

# at each stair I will iterate through the numbers ranging from 1 to maxSteps and call the function recursively

def traverse(height, maxSteps, ways):
    if height < 0:
        return 0
    
    elif height == 0:
        #ways += 1
        return 1
        
    else:
        for noSteps in range(1, maxSteps + 1):
            ways += traverse(height-noSteps, maxSteps, 0)
            
    return ways
        
print(staircaseTraversal(4,2))
