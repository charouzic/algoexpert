def sunsetViews(buildings, direction):
    # Write your code here.
    # if direction == east ==> all the buildings are facing east
        # I can do an iteration reversed values
    # direction == west ==> all the building are facing west
        # I need to do normal iteration
    
    # I'm returning the indexes of building that can see sunset
        # this is continioned by being taller that the previous building
    tallest = 0
    res = []
    noBuildings = len(buildings)
    
    if direction == "EAST":
        for idx in reversed(range(noBuildings)):
            currVal = buildings[idx]
            if currVal > tallest:
                res.insert(0, idx)
                tallest = currVal
        
    
    elif direction == "WEST":
        for idx in range(noBuildings):
            currVal = buildings[idx]
            if currVal > tallest:
                res.append(idx)
                tallest = currVal
                
    return res

## COMPLEXITY
# time -> O(n) where n is the number of buildings
# space -> O(n)